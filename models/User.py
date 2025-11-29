from db.sqlalchemy_connect import Base
from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship


class User_bs(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    written = relationship("Blog_bs",back_populates='creator')
    
    