# routes.py
from flask import Blueprint, render_template
from .models import Movie

# ✅ Create the Blueprint
routes_bp = Blueprint('routes', __name__)

# 🎞️ Home route
@routes_bp.route('/')
def index():
    # 🔍 Fetch all movies from the database
    movies = Movie.query.all()
    # 🎨 Render the homepage with movie data
    return render_template('index.html', movies=movies)

