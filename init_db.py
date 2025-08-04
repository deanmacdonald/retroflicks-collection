from app.models import db, Movie
from app.routes import app

with app.app_context():
    db.create_all()

    films = [
        Movie(
            title="Nosferatu",
            year=1922,
            genre="Horror",
            synopsis="A vampire stalks his prey in this silent era masterpiece.",
            poster_url="https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Nosferatuposter.jpg/220px-Nosferatuposter.jpg",
            video_url="https://archive.org/details/nosferatu"
        ),
        Movie(
            title="Charade",
            year=1963,
            genre="Mystery",
            synopsis="A widow is chased by several men after her husband’s fortune.",
            poster_url="https://upload.wikimedia.org/wikipedia/en/9/99/Charadeposter.jpg",
            video_url="https://archive.org/details/Charade_201303"
        ),
        Movie(
            title="Night of the Living Dead",
            year=1968,
            genre="Zombie",
            synopsis="A group of strangers fight off undead creatures in rural Pennsylvania.",
            poster_url="https://upload.wikimedia.org/wikipedia/en/4/4d/Night_of_the_Living_Dead_%281968%29_theatrical_poster.jpg",
            video_url="https://archive.org/details/night_of_the_living_dead"
        )
    ]

    db.session.bulk_save_objects(films)
    db.session.commit()
    print("🍿 Retro films added to database.")

