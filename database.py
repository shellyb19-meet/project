from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_product(name,color,picture,price,types,count,stock):
	product_object = Product(name=name, color=color, picture=picture,  price=price, types=types, count=count, stock=stock)
	session.add(product_object)
	session.commit()

def get_product_by_name(name):
	product=session.query(Product).filter_by(name=name).first()
	return product

def get_all_products():
	products = session.query(Product).all()
	return products

def create_story(title, story, name, age, gender, place, types):
	story_object = Story(title=title, story=story, name=name, age=age, gender=gender, place=place, types=types)
	session.add(story_object)
	session.commit()

def get_story_by_title(title):
	story=session.query(Story).filter_by(name=name).first()
	return story

def get_all_stories():
	stories = session.query(Story).all()
	return stories

def create_event(name,time,place,info,picture,coming):
	event_object = Event(name=name, time=time , date=date, place=place, info=info, picture=picture, coming=coming)
	session.add(event_object)
	session.commit()

def get_event_by_name(name):
	event=session.query(Event).filter_by(name=name).first()
	return event

def get_all_events():
	events = session.query(Event).all()
	return events

