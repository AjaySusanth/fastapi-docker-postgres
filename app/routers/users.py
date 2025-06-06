from sqlalchemy.orm import Session
from .. import crud, database, schemas
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix='/users',tags=['users'])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/',response_model=schemas.UserOut)
def create(user: schemas.UserCreate, db:Session = Depends(get_db)):
    return crud.create_user(db,user)

@router.get('/',response_model=list[schemas.UserOut])
def read_all(db:Session = Depends(get_db)):
    return crud.get_users(db)

@router.get('/{user_id}',response_model=schemas.UserOut)
def read_user(user_id:int, db:Session = Depends(get_db)):
    user = crud.get_user(db,user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.delete('/{user_id}')
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = crud.delete_user(db,user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return {"message":"user deleted", "user":user}



