from app import db

class Members(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    #password = db.Column(db.String(30), nullable=False)
    registration_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
            }
