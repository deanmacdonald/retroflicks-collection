# app/models.py
from app.extensions import db  # ⬅️ From the separate extensions module

class Movie(db.Model):
    __tablename__ = 'movies'  # Optional: define table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Movie {self.title} ({self.year})>"

