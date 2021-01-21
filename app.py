"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def list_users():
    """List users and show add user button."""

    users = User.query.order_by('last_name', 'first_name').all()
    return render_template("list.html", users=users)

@app.route("/users/new")
def show_add_user_form():
    """Display form to add new user"""

    return render_template("add_form.html")

@app.route("/users/new", methods=["POST"])
def add_user():
    """Create a new user in the databse"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = None if image_url == '' else image_url

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user.id}")

@app.route("/users/<int:id>")
def user_profile(id):
    """Display profile page for user"""

    user = User.query.get_or_404(id)
    return render_template("profile.html", user=user)

@app.route("/users/<int:id>/edit")
def user_edit_form(id):
    """Display edit form for user"""

    user = User.query.get_or_404(id)
    return render_template("edit_form.html", user=user)

@app.route("/users/<int:id>/edit", methods=["POST"])
def update_user(id):
    """Update user with values from edit form"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User.query.get_or_404(id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user.id}")

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user(id):
    """Delete user from database"""

    User.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(f"/")

    