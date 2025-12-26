from sqlalchemy import Column, Integer, String, Float
from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
