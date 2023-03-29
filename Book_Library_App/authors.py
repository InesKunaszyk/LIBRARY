from flask import jsonify, request

from Book_Library_App import app, db
from Book_Library_App.models import Author, AuthorSchema, author_schema
from Book_Library_App.utils import validate_json_content_type

from webargs.flaskparser import use_args


@app.route('/api/i/authors', methods=['GET'])
def get_authors():
    """"Return all authors"""
    authors = Author.query.all()
    schema_args = Author.get_schema_args(request.args.get('fields'))
    author_schema = AuthorSchema(**schema_args)
    print(schema_args)

    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records': len(authors),
    })


@app.route('/api/i/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    """Returns a single author with ID"""
    author = Author.query.get_or_404(author_id, description=f"Author with id: {author_id} not found")
    return jsonify({
        'success': True,
        'data': author_schema.dump(author),
    }), 201


@app.route('/api/i/authors', methods=['POST'])
# CODE USE WITH MARSMALLOW & WEBARGS
@validate_json_content_type
@use_args(author_schema, error_status_code=400)
def create_author(args: dict):
    """Create a new author"""
    author = Author(**args)

    db.session.add(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    }), 201

    # CODE WITHOUT USE MARSHMALLOW 'VALIDATE & VALIDATIONERROR" -> LOOAK AT DATA VALIDATION

    # data = request.get_json()
    # first_name = data.get('first_name')
    # last_name = data.get('last_name')
    # birth_date = data.get('birth_date')

    # author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date)
    # db.session.add(author)
    # db.session.commit()

    # return jsonify({
    #     'success': True,
    #     'data': 'New author has been Created'
    # }), 201


@app.route('/api/i/authors/<int:author_id>', methods=['PUT'])
@validate_json_content_type
@use_args(author_schema, error_status_code=400)
def update_author(args: dict, author_id: int):
    """Updating an author with id(id is given)"""
    author = Author.query.get_or_404(author_id, description=f"Author with id: {author_id} not found")
    author.first_name = args['first_name']
    author.last_name = args['last_name']
    author.birth_date = args['birth_date']

    db.session.commit()

    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    })


@app.route('/api/i/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    """Delete an author depending on id"""
    author = Author.query.get_or_404(author_id, description=f"Author with id: {author_id} not found")

    db.session.delete(author)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': f'Author with id: {author_id} has been deleted'
    })
