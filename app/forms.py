from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    synopsis = TextAreaField("Synopsis", validators=[DataRequired()])
    poster_url = StringField("Poster URL", validators=[DataRequired(), URL()])
    video_url = StringField("Video URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Add Movie")

