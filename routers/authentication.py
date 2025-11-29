from fastapi import APIRouter, Depends, HTTPException
from db.sqlalchemy_connect import get_db
from schemas import base_schema
from sqlalchemy.orm import Session
from models.User import User_bs
from jwt.exceptions import InvalidTokenError
from repositeries.hashing import verify_password
from repositeries.jwtauth import *
from schemas.base_schema import Token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['authentication'],prefix='/login')

@router.post('/')
def login(login:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = db.query(User_bs).filter(User_bs.email == login.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(plain_password=login.password,hashed_password=user.password):
        raise HTTPException(status_code=404, detail="User not found")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
    # return login.password