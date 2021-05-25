import os

db_URI = os.getenv('DATABASE_URL', 'postgres://localhost:5432/football_db')
secret = os.getenv('SECRET', 'This is our secret string blah blah blah')
PYTHONUNBUFFERED = 0
