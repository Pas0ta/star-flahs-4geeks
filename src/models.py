from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)
    user_name = db.Column(db.String(250), unique=False, nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(120))
    planet = db.Column(db.String(120))
    favorite_character_id = db.Column(db.Integer, db.ForeignKey('Character.id'))
    favorite_planet_id = db.Column(db.Integer, db.ForeignKey('Planet.id'))
    #relaciones para añadir y eliminar de favoritos
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship("User", foreign_keys= [user_id])
    favorite_character = db.relationship("Character", foreign_keys = [favorite_character_id])
    favorite_planet = db.relationship("Planet", foreign_keys = [favorite_planet_id])

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user.id,
            "character": self.character.id,
            "planet": self.planet.id}
class Character(db.Model):
    __tablename__ = "Character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(400))
    Favorites_id = db.Column(db.Integer)
    Birth_Year = db.Column(db.String(250), nullable=False)
    Height = db.Column(db.String(250), nullable=False)
    Mass = db.Column(db.String(250), nullable=False)
    Species = db.Column(db.String(250), nullable=False)
    Hair_Color = db.Column(db.String(250), nullable=False)
    Skin_Color =db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.name,
            "email": self.name,
            "description": self.description,
            "Birth_Year": self.Birth_Year,
            "Height": self.Height,
            "Mass": self.Mass,
            "Species": self.Species,
            "Hair_Color": self.Hair_Color,
            "Skin_Color": self.Skin_Color
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    __tablename__ = "Planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(400))
    Surface_Water = db.Column(db.String(250), nullable=True)
    Diameter = db.Column(db.String(250), nullable=True)
    position = db.Column(db.String(250), nullable=True)
    Climate = db.Column(db.String(250), nullable=True)
    Gravity = db.Column(db.String(250), nullable=True)
    Rotation_Period = db.Column(db.String(250), nullable=True)
    Orbital_Period = db.Column(db.String(250), nullable=True)
    Terrain = db.Column(db.String(250), nullable=True)
    Population = db.Column(db.String(250), nullable=True)
    
    def serialize(self):
        return {
            "id": self.name,
            "email": self.name,
            "description": self.description,
            "Surface_Water": self.Surface_Water,
            "Diameter": self.Diameter,
            "position": self.position,
            "Climate": self.Climate,
            "Gravity": self.Gravity,
            "Rotation_Period": self.Rotation_Period,
            "Orbital_Period": self.orbita,
            "Terrain": self.Terrain,
            "Population": self.Population,
            # do not serialize the password, its a security breach
        }