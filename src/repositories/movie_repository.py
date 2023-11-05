from models import Movie  # Import the Movie model
class MovieRepository:

    def get_all_movies(self):
        movies = Movie.query.all()
        return movies


from models import Movie  # Import the Movie model
class MovieRepository:
    def get_movie_by_id(self, movie_id):
        movie = Movie.query.get(movie_id)
        return movie


from models import Movie  # Import the Movie model
from app import db  # Import the SQLAlchemy DB object
class MovieRepository:
    def create_movie(self, title, director, release_year):
        new_movie = Movie(title=title, director=director, release_year=release_year)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

from models import Movie  # Import the Movie model
class MovieRepository:
    def search_movies(self, search_term):
        movies = Movie.query.filter(
            (Movie.title.ilike(f"%{search_term}%")) | 
            (Movie.director.ilike(f"%{search_term}%"))
        ).all()
        return movies



# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()