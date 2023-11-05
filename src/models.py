# TODO - Create SQLAlchemy DB and Movie model
import dbm


class Movie(db.Model):
    __tablename__ = 'movies'  # Set the table name if different

    id = dbm.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)

    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year
