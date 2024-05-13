from app import db

class Genre(db.Model):
    __tablename__ = 'genres'

    genres_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))

