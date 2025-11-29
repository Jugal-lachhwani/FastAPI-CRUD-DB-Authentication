from db.sqlalchemy_connect import Base
from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Blog_bs(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    
    creator = relationship("User_bs",back_populates='written')

        
    
    
    
