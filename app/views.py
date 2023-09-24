from flask import render_template, url_for, request, flash, redirect
from flask import current_app as app
from app import db, mail
from .models import Customer
from .forms import SignUpForm
from flask_mail import Message


@app.route("/", methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        existing_email = Customer.query.filter_by(email=email).first()
        if existing_email:
            flash(f"Email Already Exists! Please use a different email", "danger")
        else:
            db.session.add(Customer(name=name, email=email))
            db.session.commit()
            flash(f"Email entered successfully", "success")
            send_email(name, email)
            return redirect(url_for('index'))
    
    title = "Induskriti - Coming Soon"
    return render_template("index.html", title=title, form=form)

def send_email(name, email):
    recipient_name = name.split(' ')[0]
    message = Message("Test Message", recipients=[email])
    message.html = f"<h1>Hello {recipient_name}, This is <strong>Bony</strong> from the Induskriti!</h1>"
    mail.send(message)