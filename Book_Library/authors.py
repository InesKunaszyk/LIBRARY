from Book_Library import app
from flask import jsonify


@app.route('/api/i/authors', methods=['GET'])
def get_authors():
    """"Return all authors"""
    return jsonify({
        'success': True,
        'data': 'Get all authors'
    })


@app.route('/api/i/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    """Returns a single author with ID"""
    return jsonify({
        'success': True,
        'data': f'Get author with id: {author_id}'
    })


@app.route('/api/i/authors', methods=['POST'])
def create_author():
    """Create a new author"""
    return jsonify({
        'success': True,
        'data': 'New author has been Created'
    }), 201


@app.route('/api/i/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    """Updating an author with id(id is given)"""
    return jsonify({
        'success': True,
        'data': f'Author with id: {author_id} has bee updated'
    })


@app.route('/api/i/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    """Delete an author depending on id"""
    return jsonify({
        'success': True,
        'data': f'Author with id: {author_id} has been deleted'
    })
