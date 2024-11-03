#!/usr/bin/python3
"""
City model
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, prmary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
