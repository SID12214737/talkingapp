from app import app, db

# Create the database tables within the Flask application context
with app.app_context():
    db.create_all()