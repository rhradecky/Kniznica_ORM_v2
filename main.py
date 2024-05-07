from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy



main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://upkjsca8ynbl11b0ikgz:f1nKXzsR6eivAWjmQDT6i6W0E7b2vG@bdipmw29ejuoeccxynb1-postgresql.services.clever-cloud.com:50013/bdipmw29ejuoeccxynb1'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)

#from models.Author import Author
from author import Author

@main.route('/authors', methods=['GET'])
def geAuthors():
    authors = Author.query.all()
    authors_list = [author.to_dict() for author in authors]
    return jsonify(authors_list)

@main.route('/authors/<int:id>')
def get_author(id):
    author = Author.query.get(id)
    return jsonify(author.to_dict()), 200


@main.route('/authors/add', methods=['POST'])
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
@main.route('/members', methods=['GET'])
def geMembers():
    members = Members.query.all()
    members_list = [Member.to_dict() for mem in members]
    return jsonify(members_list)







#from models.User import User
#@app.route('/users', methods=['GET'])
#def getUsers







if __name__ == '__main__':
    main.run(debug=True)
