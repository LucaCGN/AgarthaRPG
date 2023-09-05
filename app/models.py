from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import sys

# Importing config variables
sys.path.append('..')  # Add the parent directory to the sys.path
from config import MYSQL_HOST, MYSQL_DB_NAME, MYSQL_USER, MYSQL_PASSWORD

# Initialize database
DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB_NAME}'
engine = create_engine(DATABASE_URI, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
db_session = scoped_session(Session)

Base = declarative_base()
Base.query = db_session.query_property()

class AccountInfo(Base):
    __tablename__ = 'account_info'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    user_surname = Column(String(50))
    user_birthday = Column(Date)
    user_email = Column(String(200), unique=True)
    user_password = Column(String(64))
    user_verified = Column(String(3))
    user_code = Column(Integer)
