from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/education')
def education():
    return render_template('education.html')


@main.route('/gaming')
def gaming():
    return render_template('gaming.html')


@main.route('/linux')
def linux_quiz():
    return render_template('linux.html')


@main.route('/shell')
def shell_quiz():
    return render_template('shell.html')


@main.route('/sql')
def sql_quiz():
    return render_template('sql.html')


@main.route('/devops-basic')
def devops_basic():
    return render_template('devops-basic.html')


@main.route('/devops-intermediate')
def devops_intermediate():
    return render_template('devops-intermediate.html')


@main.route('/devops-advanced')
def devops_advanced():
    return render_template('devops-advanced.html')


@main.route('/news')
def news():
    return render_template('news.html')


@main.route('/marketing')
def marketing():
    return render_template('marketing.html')


@main.route('/webdev')
def webdev():
    return render_template('webdev.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/verification')
def verification():
    return render_template('verification.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/privacy')
def privacy():
    return render_template('privacy.html')


@main.route('/terms')
def terms():
    return render_template('terms.html')


@main.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    print(
        f"Contact form submitted by {name}, Email: {email}, Subject: {subject}, Message: {message}")

    flash("Your message has been sent successfully!", "success")
    return redirect(url_for("main.contact"))
