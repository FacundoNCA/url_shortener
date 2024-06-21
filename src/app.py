from flask import Flask, render_template, redirect, request, jsonify
from models import db, URLS
from utils import generate_short_url

from config import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/url_shortener'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        url_original = request.json.get("url_original")
        
        short_url = generate_short_url()
        new_url = URLS(url_original=url_original, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()
        
        return jsonify({ "short_url": short_url, "url_original": url_original })

    return render_template("index.html")

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = URLS.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.url_original)

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.config.from_object(config['development'])
    app.run()

