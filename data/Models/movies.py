from data.db import Base
import sqlalchemy as sa


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = sa.Column(sa.String(5), primary_key=True)
    movie_title = sa.Column(sa.String(250), nullable=False)
    movie_year = sa.Column(sa.Integer, nullable=False)
    IMDB_rating = sa.Column(sa.Float, nullable=False)
    IMDB_votes = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return f'{self.movie_title} - {self.movie_year}'
