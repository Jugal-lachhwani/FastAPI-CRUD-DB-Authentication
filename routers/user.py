from fastapi import APIRouter, Depends
from schemas.blog import *
from typing import List
from sqlalchemy.orm import Session
from db.sqlalchemy_connect import get_db
from repositeries import user_repo,jwtauth

router = APIRouter(tags=['users'],prefix='/user')

@router.post('/create_user',status_code=201,response_model=response_user)
def create_user(user:user,db: Session = Depends(get_db)):
    return user_repo.create_new_user(user,db)

@router.get('/get_user/',response_model=List[response_user])
def get_users(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)