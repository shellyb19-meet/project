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

def create_story(title, story, name, age, gender, place, types, week):
	story_object = Story(title=title, story=story, name=name, age=age, gender=gender, place=place, types=types, week=week)
	session.add(story_object)
	session.commit()

def get_story_by_title(title):
	story=session.query(Story).filter_by(name=name).first()
	return story

def get_all_stories():
	stories = session.query(Story).all()
	return stories


def get_week_story():
	story=session.query(Story).filter_by(week=True).first()
	return story

def get_upcoming():
	events=session.query(Event).filter_by(soon=True).all()
	return event

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

create_story("title", "story story story story", "shelly" , 16, "female", "jerusalem", "types")

create_story("title2", "story story story story", "bamba" , 163, "female", "tel aviv", "types2")

create_story("title3", "story story story story", "shorts" , 12, "male", "jerusalem", "types")
, 