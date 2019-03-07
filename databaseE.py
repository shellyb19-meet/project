from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///events.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_event(name,time,place,info,picture,coming):
	event_object = Event(name=name, time=time , place=place, info=info, picture=picture, coming=coming)
	session.add(event_object)
	session.commit()

def get_event_by_name(name):
	event=session.query(Event).filter_by(name=name).first()
	return event

def get_all_events():
	events = session.query(Event).all()
	return events
