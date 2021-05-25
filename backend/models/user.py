from app import db
from models.base import BaseModel

# from sqlalchemy.ext.hybrid import hybrid_property
# from environment.config import secret


from datetime import *
# import jwt


class User(db.Model, BaseModel):

    __tablename__ = 'users'

    firstname = db.Column(db.String(20), nullable=False, unique=False)
    lastname = db.Column(db.String(20), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    role = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=False)
    company = db.Column(db.String(50), nullable=False, unique=False)
