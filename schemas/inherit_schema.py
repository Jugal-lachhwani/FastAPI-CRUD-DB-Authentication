from pydantic import BaseModel

class inherit_blog_schema(BaseModel):
    title : str
    body : str
    class Config():
        orm_mode = True
        
class inherit_user_schema(BaseModel):
    name : str
    email : str
    
    class Config():
        orm_mode = True  