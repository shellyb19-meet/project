from modelP import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///places.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_product(name,color,picture,price,types,count,stock):
	product_object = Place(name=name, color=color, picture=picture,  price=price, types=types, count=count, stock=stock)
	session.add(product_object)
	session.commit()

def get_product_by_name(name):
	product=session.query(Product).filter_by(name=name).first()
	return product

def get_all_products():
	products = session.query(Product).all()
	return products

