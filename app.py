from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://upkjsca8ynbl11b0ikgz:f1nKXzsR6eivAWjmQDT6i6W0E7b2vG@bdipmw29ejuoeccxynb1-postgresql.services.clever-cloud.com:50013/bdipmw29ejuoeccxynb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from author import Author
from book import Book
from members import Members
from genres import Genre

@app.route('/')
def command_list():
    return ('<big>Zoznam dostupnych prikazov<small><BR>/authors <BR>/author/ID <BR>/authors/add <BR>/books<BR>/books/ID<BR>/books/add<BR>/books/update<BR>/books/delete/ID')
    #return ('<big>Zoznam dostupnych prikazov<small><BR><a href=„https://just-eleonora-apmedia-9fcf8fe0.koyeb.app/authors>/authors"</a')



@app.route('/authors', methods=['GET'])
def ge_Authors():
    authors = Author.query.all()
    authors_list = [author.to_dict() for author in authors]
    return jsonify(authors_list)

@app.route('/author/<int:id>')
def get_author_id(id):
    author = Author.query.get(id)
    return jsonify(author.to_dict()), 200

@app.route('/authors/add', methods=['POST'])
def add_authors():
  print(request)
  new_author = Author(name=request.json['name'], bio=request.json['bio'])
  db.session.add(new_author)
  db.session.commit()
  return jsonify(new_author.to_dict()), 201


@app.route('/members', methods=['GET'])
def get_Members():
    members = Members.query.all()
    members_list = [member.to_dict() for member in members]
    return jsonify(members_list)




@app.route('/books', methods=['GET'])
def get_Books():
  books = Book.query.all()
  books_list = [book.to_dict() for book in books]
  return jsonify(books_list)

@app.route('/books/<int:id>')
def get_Books_id(id):
    book = Book.query.get(id)
    return jsonify(book.to_dict()), 200

@app.route('/books/add', methods=['POST'])
def add_books():
    print(request)
    new_book = Book(title=request.json['title'],author_id = request.json['author_id'],genre_id =  request.json['genre_id'],isbn =  request.json['isbn'],publication_year = request.json['publication_year'],copies = request.json['copies'])
    db.session.add(new_book)
    db.session.commit()
    print(new_book)
    return jsonify(new_book.to_dict()), 201




@app.route('/books/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
         return jsonify({'error': 'Book not found'}), 404







if __name__ == '__main__':
    app.run(debug=True)
