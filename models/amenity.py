#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_id = Column(String(255), ForeignKey('places.id'), nullable=False)
    related_places = relationship(
        "Place",
        back_populates="associated_amenities",
    )
