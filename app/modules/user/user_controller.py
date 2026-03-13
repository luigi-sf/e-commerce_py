from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.core.database import get_db
from app.modules.user.user_repository import UserRepository
from app.modules.user.user_service import UserService
from app.modules.user.user_schema import UserCreate, UserUpdate, UserResponse

from app.core.security.dependencies import get_current_user, require_role
from app.models.user import User


router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)


@router.post("/", response_model=UserResponse, status_code=201)
def create(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create(user)


@router.get("/", response_model=list[UserResponse])
def list(
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(require_role("admin"))
):
    return service.list()


@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)): #so precisa estar logado
    return current_user


@router.put("/me", response_model=UserResponse)
def update_me(
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    return service.update(current_user.id, user)


@router.delete("/me", response_model=UserResponse)
def delete_me(
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    return service.delete(current_user.id)


@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(require_role("admin"))
):
    return service.get_by_id(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update(
    user_id: UUID,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    return service.update(user_id, user, current_user)


@router.delete("/{user_id}", response_model=UserResponse)
def delete(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
    current_user: User = Depends(require_role("admin"))
):
    return service.delete(user_id)