from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), nullable=False, unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_supperuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")