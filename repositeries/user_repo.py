from fastapi import HTTPException
from models.User import User_bs
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def create_new_user(user,db):
    password = get_password_hash(password=user.password)
    new_user = User_bs(name=user.name,email=user.email,password=password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db):
    users = db.query(User_bs).all()
    if not users:
        raise HTTPException(status_code=404,detail=f"No ID is available")
    return users