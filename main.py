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
    return Authors





#from models.User import User
#@app.route('/users', methods=['GET'])
#def getUsers







if __name__ == '__main__':
    main.run()
