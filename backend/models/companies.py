from app import db
from models.base import BaseModel
from models.user_company import user_company_join
from models.user import User


# from sqlalchemy.ext.hybrid import hybrid_property
# from environment.config import secret


from datetime import *
# import jwt


class Company(db.Model, BaseModel):

    __tablename__ = 'companies'

    name = db.Column(db.String(30), nullable=False, unique=True)
    users = db.relationship(
        'User', secondary=user_company_join, backref='companies')
