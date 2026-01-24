from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app.db import Base

#Database Tables
class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    category = Column(String)
    external_id = Column(String, index=True) #will only hold steam game id for now

