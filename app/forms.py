from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class MovieSearchForm(FlaskForm):
    query = StringField("Search for a movie")
    decade = SelectField("Decade", choices=[
        ("All", "All"),
        ("1920s", "1920s"),
        ("1940s", "1940s"),
        ("1950s", "1950s"),
        ("1980s", "1980s")
    ])
    genre = SelectField("Genre", choices=[
        ("All", "All"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Sci-Fi", "Sci-Fi"),
        ("Musical", "Musical"),
        ("Thriller", "Thriller"),
        ("Romance", "Romance")
    ])
    submit = SubmitField("🎬 Search")

