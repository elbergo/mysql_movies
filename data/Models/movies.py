from data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

movies_genres = sa.Table('movies_genres', Base.metadata,
    sa.Column('movies_movie_id', sa.String(5), sa.ForeignKey('movies.movie_id')),
    sa.Column('genres_genre_id', sa.Integer, sa.ForeignKey('genres.genre_id')),
)

class Movie(Base):
    __tablename__ = 'movies'

    movie_id = sa.Column(sa.String(5), primary_key=True)
    movie_title = sa.Column(sa.String(250), nullable=False)
    movie_year = sa.Column(sa.Integer, nullable=False)
    IMDB_rating = sa.Column(sa.Float, nullable=False)
    IMDB_votes = sa.Column(sa.Integer, nullable=False)

    genres = relationship('Genre', secondary=movies_genres)

    def __repr__(self):
        return f'{self.movie_title} - {self.movie_year}'


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = sa.Column(sa.Integer, primary_key=True)
    genre_name = sa.Column(sa.String(150), nullable=False)

    def __repr__(self):
        return self.genre_name

"""
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table)

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
"""