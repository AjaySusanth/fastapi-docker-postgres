from sqlalchemy.orm import Session
from . import models,schemas

def create_user(db:Session, user:schemas.UserCreate):
    db_user = models.User(name=user.name,email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:Session):
    return db.query(models.User).all()

def get_user(db:Session,user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db:Session, user_id:int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
