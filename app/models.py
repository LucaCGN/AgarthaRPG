# models.py

from sqlalchemy import Column, Integer, String, Date, Boolean

class AccountInfo(Base):
    __tablename__ = 'account_info'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    user_surname = Column(String(50))
    user_birthday = Column(Date)
    user_email = Column(String(200), unique=True)
    user_password = Column(String(64))
    user_verified = CColumn(String(3))
    user_code = Column(Int(6))
