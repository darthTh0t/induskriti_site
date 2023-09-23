from flask import render_template, url_for, request, flash, redirect
from flask import current_app as app
from app import db
from .models import Customer
from .forms import SignUpForm


@app.route("/", methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        existing_email = Customer.query.filter_by(email=email).first()
        if existing_email:
            flash(f"Email Already Exists! Please use a different email", "danger")
        else:
            db.session.add(Customer(email=email))
            db.session.commit()
            flash(f"Email entered successfully", "success")
            return redirect(url_for('index'))
    
    title = "Induskriti - Coming Soon"
    return render_template("index.html", title=title, form=form)