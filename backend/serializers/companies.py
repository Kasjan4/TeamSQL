from app import ma
from serializers.base import BaseSchema
from models.companies import Company
from marshmallow import fields


class CompanySchema(ma.SQLAlchemyAutoSchema, BaseSchema):

    class Meta:
        model = Company
        load_instance = True

        # exclude = ('password_hash',)
        # load_only = ('email', 'password')

    # password = fields.String(required=True)
