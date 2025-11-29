from fastapi import APIRouter, Depends
from schemas.blog import *
from typing import List
from sqlalchemy.orm import Session
from db.sqlalchemy_connect import get_db
from repositeries import blog_repo, jwtauth,outh

router = APIRouter(tags=['blogs'],prefix='/blog')

@router.post('/create',status_code=201,response_model=response)
def create_blog(blog:Blog,db: Session = Depends(get_db), get_current_user = Depends(outh.get_current_user)):
    return blog_repo.create_new_blog(blog,db)

@router.get('/get_blog/',response_model=List[response])
def get_blog(db: Session = Depends(get_db), get_current_user = Depends(outh.get_current_user)):
    return blog_repo.get_all_blogs(db)

@router.get('/get_blog/{id}',response_model=response)
def get_blog(id:int,db: Session = Depends(get_db), get_current_user = Depends(outh.get_current_user)):
    return blog_repo.get_blog_by_id(id,db)

@router.put('/update_blog/{id}',response_model=response)
def update_blog(id:int,blog:Blog,db: Session = Depends(get_db), get_current_user = Depends(outh.get_current_user)):
    return blog_repo.update_blog_by_id(id,blog,db)

@router.delete('/delete_blog/{id}')
def delete_blog(id:int,db: Session = Depends(get_db), get_current_user = Depends(outh.get_current_user)):
    return blog_repo.delete_blog_by_id(id,db)