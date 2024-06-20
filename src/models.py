from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLS(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url_original = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique = True, nullable=False)