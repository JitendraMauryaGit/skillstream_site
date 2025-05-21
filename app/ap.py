from flask import Flask, render_template
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables


def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    from app.routes import main
    app.register_blueprint(main)

    return app


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/gaming')
def gaming():
    return render_template('gaming.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/marketing')
def marketing():
    return render_template('marketing.html')


@app.route('/webdev')
def webdev():
    return render_template('webdev.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


if __name__ == '__main__':
    app.run(debug=True)
