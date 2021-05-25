from flask import Blueprint, request
from models.companies import Company
from serializers.companies import CompanySchema


companies_schema = CompanySchema()

router = Blueprint(__name__, 'users')


@router.route('/users/<int:id>', methods=['GET'])
def get_single_company(id):

    company = Company.query.get(id)

    if not company:
        return {'message': 'User not available'}, 404

    return companies_schema.jsonify(company), 200
