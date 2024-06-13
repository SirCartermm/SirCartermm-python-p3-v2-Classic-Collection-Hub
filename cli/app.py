#app.py
import click
from sqlalchemy.orm import sessionmaker
from models.supercar import Base, Supercar, User, Vote, Comment

engine = create_engine('sqlite:///supercars.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)