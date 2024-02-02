# import os
# import sys
# from typing import List
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine

# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column

# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(64), unique=True, nullable=False)
#     password = Column(String, nullable=False)
#     Favorite = relationship("favorite", back_populates = "User")

# class Favorite(Base):
#     __tablename__ = 'favorite'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(ForeignKey("user.id"))
#     planet_id = Column(ForeignKey)("planets.id")
#     character_id = Column(ForeignKey)("person.id")
#     user = relationship("User", back_populates = "Favorite")
#     planet = relationship("Planets", back_populates = "Favorite")


# class Person(Base):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True)
#     Favorites = relationship("favorites", back_populates="person") 
#     name = Column(String)
#     birth_year = Column(String)
#     height = Column(Integer)
#     mass = Column(Integer)


# class Planets(Base):
#     __tablename__ = 'planets'
#     id = Column(Integer, primary_key=True)
#     Favorites = relationship("favorites", back_populates="planets")
#     name = Column(String)
#     gravity = Column(Integer)
#     population = Column(Integer)
#     terrain = Column(String)




import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String, nullable=False)
    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))
    character_id = Column(Integer, ForeignKey("person.id"))
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    character = relationship("Person", back_populates="favorites")

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(String)
    height = Column(Integer)
    mass = Column(Integer)
    favorites = relationship("Favorite", back_populates="character")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gravity = Column(String)  # Changed from Integer to String to accommodate values like '1 standard'
    population = Column(Integer)
    terrain = Column(String)
    favorites = relationship("Favorite", back_populates="planet")

# Drawing the ER diagram would require having eralchemy installed and properly configured in your environment.
# render_er(Base, 'diagram.png')
## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')