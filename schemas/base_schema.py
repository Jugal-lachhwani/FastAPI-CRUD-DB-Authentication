from pydantic import BaseModel

class user(BaseModel):
    name : str
    email : str
    password : str

class Blog(BaseModel):
    title : str
    body : str
    
class login(BaseModel):
    username : str
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None