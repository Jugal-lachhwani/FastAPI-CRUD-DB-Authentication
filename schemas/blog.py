from pydantic import BaseModel
# from schemas.user import response_user
from typing import List

class Blog(BaseModel):
    title : str
    body : str

class inherit_blog_schema(BaseModel):
    title : str
    body : str
    class Config():
        orm_mode = True
        

class response_user(BaseModel):
    name : str
    email : str
    written : List[inherit_blog_schema]
    
    class Config():
        orm_mode = True    

class inherit_user_schema(BaseModel):
    name : str
    email : str
    
    class Config():
        orm_mode = True    

class response(BaseModel):
    title : str
    body : str
    creator : inherit_user_schema
    class Config():
        orm_mode = True
        
class user(BaseModel):
    name : str
    email : str
    password : str
    
    
