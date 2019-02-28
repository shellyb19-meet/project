from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
	__tablename__ = "products"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	color=Column(String)
	picture=Column(String)
	price=Column(Integer)
	types=Column(String)
	count=Column(Integer)
	stock=Column(String)