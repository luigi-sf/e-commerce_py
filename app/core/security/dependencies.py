from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer # extrair o token do header
from app.core.security.token import decode_token
from app.models.black_list import TokenBlacklist
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/auth/login'
)


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    black_list = db.query(TokenBlacklist).filter(
        TokenBlacklist.token == token
    ).first()

    if black_list:
        raise HTTPException(401, "Token revoked")

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(401, "Invalid token")

    user = db.query(User).filter(
        User.id == payload["user_id"]
    ).first()

    if not user:
        raise HTTPException(404, "User not found")

    return user


def require_role(roles: list[str]):

    def role_checker(user = Depends(get_current_user)):

        if user.get("role") not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )

        return user

    return role_checker