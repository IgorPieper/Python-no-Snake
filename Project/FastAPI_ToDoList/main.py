from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Generator, List, Optional

from fastapi import Depends, FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todos"

    todo_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic schemas
class TodoBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=10_000)
    completed: bool = False


class TodoCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=10_000)
    completed: bool = False


class TodoUpdate(BaseModel):
    content: Optional[str] = Field(None, min_length=1, max_length=10_000)
    completed: Optional[bool] = None


class TodoOut(TodoBase):
    todo_id: int

    class Config:
        from_attributes = True


# FastAPI application
@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="ToDo API",
    description="A simple FastAPI + SQLite CRUD service for managing ToDo items.",
    version="1.0.0",
    lifespan=lifespan,
)


# Routes
@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    return {"message": "Welcome to the ToDo API. Visit /docs for the interactive API documentation."}


@app.get("/todos", response_model=List[TodoOut], tags=["todos"])
def get_all_todos(db: Session = Depends(get_db)) -> List[TodoOut]:
    todos = db.query(Todo).order_by(Todo.todo_id.asc()).all()
    return todos


@app.get("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def get_todo(
    todo_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
) -> TodoOut:
    todo = db.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


@app.post("/todos", response_model=TodoOut, status_code=status.HTTP_201_CREATED, tags=["todos"])
def create_todo(payload: TodoCreate, db: Session = Depends(get_db)) -> TodoOut:
    todo = Todo(content=payload.content, completed=payload.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.put("/todos/{todo_id}", response_model=TodoOut, tags=["todos"])
def update_todo(
    payload: TodoUpdate,
    todo_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
) -> TodoOut:
    todo = db.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    if payload.content is not None:
        todo.content = payload.content
    if payload.completed is not None:
        todo.completed = payload.completed

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
def delete_todo(
    todo_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
) -> None:
    todo = db.get(Todo, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return None
