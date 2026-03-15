# 🛒 E-Commerce API

Backend de uma API de e-commerce desenvolvida com **FastAPI**, utilizando arquitetura modular baseada em **Service + Repository**.

O projeto implementa autenticação, gerenciamento de usuários, sellers e produtos, servindo como base para um marketplace.

---

# 🚀 Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* Poetry
* Token Blacklist
* Uvicorn

---

# 📦 Estrutura do Projeto

```
app
 ├── core
 │   ├── database.py
 │   └── security
 │
 ├── models
 │   ├── user.py
 │   ├── seller.py
 │   └── product.py
 │
 ├── modules
 │   ├── auth
 │   ├── user
 │   ├── seller
 │   └── product
 │
 ├── schemas
 └── main.py

scripts
 ├── reset_db.py
 └── seed_admin.py
```

---

# ⚙️ Instalação

Clone o repositório:

```
git clone https://github.com/luigi-sf/back_e-Commerce.git
```

Entre na pasta:

```
cd back_e-Commerce
```

Instale as dependências:

```
poetry install
```

---

# ▶️ Rodando o Projeto

Inicie o servidor:

```
make start
     ou
poetry run uvicorn main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

Documentação automática:

```
http://localhost:8000/docs
```

---

🔐 Autenticação

A API utiliza JWT (JSON Web Token) para autenticação.

Fluxo de autenticação:

1️⃣ Usuário cria conta
2️⃣ Usuário faz login
3️⃣ Recebe um access token
4️⃣ Usa o token para acessar rotas protegidas

Header necessário:

Authorization: Bearer TOKEN
🚪 Logout Seguro (Token Blacklist)

O projeto implementa blacklist de tokens para garantir logout seguro.

Quando um usuário faz logout:

o token JWT é adicionado à blacklist

tokens presentes na blacklist não podem mais acessar rotas protegidas

Isso evita que tokens roubados ou antigos continuem válidos.

Fluxo:

Login → recebe token
Logout → token vai para blacklist
Request com token → verificado contra blacklist

# 👤 Usuários

Endpoints principais:

```
POST   /auth/register
POST   /auth/login
GET    /users/me
```

---

# 🏪 Sellers

Cada usuário pode criar uma loja (seller).

```
POST   /sellers
GET    /sellers
GET    /sellers/{id}
```

---

# 📦 Produtos

Produtos pertencem a um seller.

```
POST   /products
GET    /products
GET    /products/{id}
GET    /products/me
PUT    /products/{id}
DELETE /products/{id}
```

---

# 🧪 Scripts de Desenvolvimento

Resetar banco de dados:

```
make reset
```

ou

```
poetry run python -m scripts.reset_db
```

Criar admin:

```
poetry run python -m scripts.seed_admin
```

---

# 🧠 Arquitetura

O projeto segue o padrão:

```
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
```

Isso permite:

* separação de responsabilidades
* código mais testável
* escalabilidade do projeto

---

# 📌 Funcionalidades Implementadas

* Autenticação JWT
* Registro e login de usuários
* Criação de sellers
* CRUD de produtos
* Autorização por usuário
* Reset de banco para desenvolvimento
* Seed de administrador

---

# 🔮 Próximos Passos

* Categorias de produtos
* Upload de imagens
* Sistema de pedidos
* Carrinho de compras
* Paginação e filtros de produtos

---

# 👨‍💻 Autor

Luigi Felicio

GitHub:
https://github.com/luigi-sf
