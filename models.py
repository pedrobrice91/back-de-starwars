
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email =  db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=True)
    films_Favorite = db.relationship("Films_Favorite")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

class Films_Favorite(db.Model):
    __tablename__ = "films_Favorite"
    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.String)
    title = db.Column(db.String)
    director = db.Column(db.String)
    release_date = db.Column(db.String(200), nullable=False, unique=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

    def serialize(self):
        return {
            "id": self.id,
            "episode_id": self.first_name,
            "title": self.last_name,
            "director": self.email,
            "release_date": self.created_at
        }

class People_Favorite(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    id_user = db.Colum(db.Integer, foren_key)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.first_name,
            "url": self.last_name
        }

class Planets_Favorite(db.Model):
    __tablename__ = "favorite_planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }

class Species_Favorite(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    id_user = db.Colum(db.Integer, foren_key)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.first_name,
            "url": self.last_name
        }

class Starships_Favorite(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    id_user = db.Colum(db.Integer, foren_key)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.first_name,
            "url": self.last_name,
            "id_user": self.email
        }

class Vehicles_Favorite(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    id_user = db.Colum(db.Integer, foren_key)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "created_at": self.created_at
        }
