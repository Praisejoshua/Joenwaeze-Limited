from web import app, db
from flask import render_template, redirect, flash, url_for
from web.models import User, ContactMessage
from web.forms import LoginForm, ContactForm, RegisterForm
from web.utility import send_message


# home route
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

# About route
@app.route("/about")
def about_page():
    return render_template("about.html")

# contact page
@app.route("/contact", methods = ["GET", "POST"])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        # process form 
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.text.data

        save_mail = ContactMessage(first_name = first_name,
                                   last_name = last_name,
                                   email = email,
                                   message = message        
                                   )
        db.session.add(save_mail)
        db.session.commit()
        flash("Message sent successfully", "success")
        # send message
        send_message(
            subject= "New message from JOENWAEZE LIMITED",
            sender=email,
            recipients=["praizjoshua@gmail.com"],
            body=message
        )
    return render_template("contact.html", form=form)


# products page
@app.route("/products")
def products_page():
    return render_template("products.html")


# Register Page
@app.route("/register", methods = ["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_create = User(
            username = form.username.data,
            email = form.email.data,
            hashed_password = form.password1.data
        )
        db.session.add(user_create)
        db.session.commit()
        return redirect(url_for("home_page"))
    return render_template("register.html", form = form)

# Login Page
@app.route("/login", methods = ["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        dummy_user = User(username = "jj", email="jj@gmail.com", hashed_password  = "ehtx7132" )
        db.session.add(dummy_user)
        # db.session.commit()
        flash("Dummy user created", category='success')
        return redirect(url_for("home_page"))
    return render_template("login.html", form = form)

@app.route("/service", methods=["GET", "POST"])
def service_page():
    form = ContactForm()
    if form.validate_on_submit():
        # Process form
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.text.data

        save_mail = ContactMessage(first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   message=message)
        db.session.add(save_mail)
        db.session.commit()
        flash("Message sent successfully", "success")
        
        # Send message
        send_message(
            subject="New message from JOENWAEZE LIMITED",
            sender=email,
            recipients=["praizjoshua@gmail.com"],
            body=message
        )
        return redirect(url_for('service_page'))  

    return render_template("service.html", form=form)
