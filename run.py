# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # 🚀 Start the Flask server
    app.run(debug=True)

