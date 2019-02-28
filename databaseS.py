from modelS import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///stories.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

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

