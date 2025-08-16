"""This allows Gunicorn to serve the app in production...123"""

from app import create_app

app = create_app()
