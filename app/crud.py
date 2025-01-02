from sqlalchemy.orm import Session
from . import models, schemas, security
from typing import Optional

def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str) -> Optional[models.User]:
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user


def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, user_id: int, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()

def create_task(db: Session, task: schemas.TaskCreate, user_id: int) -> models.Task:
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int) -> Optional[models.Task]:
    db_task = get_task(db, user_id, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int) -> Optional[models.Task]:
    db_task = get_task(db, user_id, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

def get_summary(db: Session, user_id: int) -> schemas.TaskSummary:
    completed = db.query(models.Task).filter(models.Task.completed == True, models.Task.owner_id == user_id).count()
    pending = db.query(models.Task).filter(models.Task.completed == False, models.Task.owner_id == user_id).count()
    return schemas.TaskSummary(completed=completed, pending=pending)
