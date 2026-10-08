# TODO-API

A simple FastAPI-based todo application with user authentication and PostgreSQL integration.

## Features
- User signup and login with JWT authentication
- Create, read, update, and delete todo items
- SQLAlchemy ORM with PostgreSQL
- Pydantic request/response validation
- FastAPI docs available automatically

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (PyJWT)
- Pydantic

## Project Structure
```bash
TODO-API/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── utils.py
│   ├── helper_func.py
│   └── routers/
│       ├── auth.py
│       ├── todos.py
│       └── users.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup
```bash
git clone https://github.com/rajat9560r-cloudRajat/TODO-API.git
cd TODO-API
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Environment Variables
```env
URL = postgresql://<username>:<password>@localhost/<database_name>
SECRET_KEY = "generate_with_openssl_rand_hex_32"
ALGORITHM = "HS256"
```

## Run
```bash
uvicorn app.main:app --reload
```

API docs will be available at:
- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

## Main Endpoints
- `POST /users/` - create user
- `POST /auth/login` - login and receive token
- `GET /todos/` - list todos
- `POST /todos/` - create todo
- `PUT /todos/{id}` - update todo
- `DELETE /todos/{id}` - delete todo

## Notes
This project is a beginner-friendly backend API for learning CRUD operations, authentication, and database integration in Python.
