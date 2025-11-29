from schemas import inherit_schema
from pydantic import BaseModel
from typing import List

class response(BaseModel):
    title : str
    body : str
    creator : inherit_schema.inherit_user_schema
    class Config():
        orm_mode = True
        
class response_user(BaseModel):
    name : str
    email : str
    written : List[inherit_schema.inherit_blog_schema]
    
    class Config():
        orm_mode = True 