from flask import jsonify, session

from Book_Library_App import db

from marshmallow import Schema, fields, validates, ValidationError
from marshmallow.validate import Length

from datetime import datetime


class Author(db.Model):
    # __tablename__ = 'authors'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.first_name}  {self.last_name}'

    @staticmethod
    def get_schema_args(fields: str):
        schema_args = {'many': True}
        print(fields)
        author = session.query(Author).all()
        a = Author.__table__.columns
        print(author)
        print(a)

        # for a in author:
        #     return print(a)

        if fields:
            schema_args['only'] = [field for field in fields.split(',') if fields in Author.__table__.columns]
        return schema_args



class AuthorSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=Length(max=50))
    last_name = fields.String(required=True)
    birth_date = fields.Date('%d-%m-%Y', required=True)

    @validates('birth_date')
    def validate_birth_date(self, value):
        if value > datetime.now().date():
            raise ValidationError(f"Birth Date must be lower than {datetime.now().date()} ")


author_schema = AuthorSchema()
