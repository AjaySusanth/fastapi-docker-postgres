from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DB_URL = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)