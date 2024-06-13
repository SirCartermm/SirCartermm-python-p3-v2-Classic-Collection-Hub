# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database URL
DATABASE_URL = "postgresql://user:password@host:port/dbname"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db = Session()