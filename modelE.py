from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Event(Base):
	__tablename__ = "events"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	time=Column(String)
	place=Column(String)
	info=Column(String)
	picture=Column(String)
	coming=Column(Boolean)