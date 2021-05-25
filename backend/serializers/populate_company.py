from app import ma
from serializers.base import BaseSchema
from marshmallow import fields
from models.companies import Company


class PopulateCompanySchema(ma.SQLAlchemyAutoSchema, BaseSchema):

    class Meta:
        model = Company
        load_instance = True

        users = fields.Nested('UserSchema', many=True)
