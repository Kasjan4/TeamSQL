from app import db

user_company_join = db.Table('company_users',
                             db.Column('user_id', db.Integer, db.ForeignKey(
                                 'users.id'), primary_key=True),
                             db.Column('company_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True))
