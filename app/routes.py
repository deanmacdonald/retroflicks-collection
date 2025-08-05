from flask import Blueprint, render_template, request
from app.models import Movie
from app.forms import MovieSearchForm
from app import db

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    form = MovieSearchForm()
    query = form.query.data
    selected_decade = form.decade.data
    selected_genre = form.genre.data

    # Start with all movies
    movies_query = Movie.query

    # Apply filters if present
    if query:
        movies_query = movies_query.filter(Movie.title.ilike(f"%{query}%"))
    if selected_decade and selected_decade != "All":
        movies_query = movies_query.filter_by(decade=selected_decade)
    if selected_genre and selected_genre != "All":
        movies_query = movies_query.filter_by(genre=selected_genre)

    movies = movies_query.all()

    return render_template("index.html", form=form, movies=movies)

