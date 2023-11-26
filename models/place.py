#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id", ondelete='CASCADE', onupdate='CASCADE'),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id", ondelete='CASCADE', onupdate='CASCADE'),
           primary_key=True, nullable=False),
)

class Place(BaseModel, Base):
    """Represents a Place for a MySQL database"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    associated_amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="related_places",
    )

    @property
    def amenities_list(self):
        """Property method to retrieve amenities."""
        return [amenity.name for amenity in self.associated_amenities]

    @amenities_list.setter
    def amenities_list(self, amenities):
        """Property method to set amenities."""
        if isinstance(amenities, Amenity):
            if amenities not in self.associated_amenities:
                self.associated_amenities.append(amenities)
        else:
            for amenity in amenities:
                if isinstance(amenity, Amenity):
                    if amenity not in self.associated_amenities:
                        self.associated_amenities.append(amenity)
