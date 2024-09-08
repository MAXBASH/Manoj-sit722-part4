from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://projectpart4_ls7i_user:vFNSd3yLz7fFVbSaztFvqHUpcxnt3ZXs@dpg-creidqggph6c73ese8g0-a.oregon-postgres.render.com/projectpart4_ls7i"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
