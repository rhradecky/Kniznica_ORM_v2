from app import db
#from author import Author


class Book(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    isbn = db.Column(db.String(13))
    publication_year = db.Column(db.Integer)
    copies = db.Column(db.Integer, default=1)

    author = db.relationship("Author", back_populates="books")
    genre = db.relationship("Genre", backref="books")


    def to_dict(self):
        return {
            "book_id" : self.book_id,
            "title" : self.title,
            "author_id": self.author_id,
            "genre_id": self.genre_id,
            "isbn": self.isbn,
            "publication_year": self.publication_year,
            "copies": self.copies
            }

