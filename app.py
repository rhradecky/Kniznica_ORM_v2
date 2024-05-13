from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://upkjsca8ynbl11b0ikgz:f1nKXzsR6eivAWjmQDT6i6W0E7b2vG@bdipmw29ejuoeccxynb1-postgresql.services.clever-cloud.com:50013/bdipmw29ejuoeccxynb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from models.Author import Author
from author import Author

@app.route('/authors', methods=['GET'])
def geAuthors():
    authors = Author.query.all()
    authors_list = [author.to_dict() for author in authors]
    return jsonify(authors_list)

@app.route('/authors/<int:id>')
def get_author(id):
    author = Author.query.get(id)
    return jsonify(author.to_dict()), 200


@app.route('/authors/add', methods=['POST'])
def add_authors():
    print(request)
    new_authors = {
        'author_id': author[-1]['author_id'] + 1,
        'name': request.json['name'],
        'bio': request.json['bio']
    }
    author.append(new_authors)
    return jsonify(new_authors), 201

from members import Members
@app.route('/members', methods=['GET'])
def geMembers():
    members = Members.query.all()
    members_list = [Member.to_dict() for mem in members]
    return jsonify(members_list)
















if __name__ == '__main__':
    app.run(debug=True)
