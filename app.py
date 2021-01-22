"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User, Post

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
    
    try:
        db.session.add(user)
        db.session.commit()
        flash("New user added", "success")
    except:
        flash("There was an error adding the user", "error")

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

    try:
        db.session.add(user)
        db.session.commit()
        flash("User updated", "success")
    except:
        flash("There was an error updating the user", "error")

    return redirect(f"/users/{user.id}")

@app.route("/users/<int:id>/delete", methods=["POST"])
def delete_user(id):
    """Delete user from database"""

    try:
        User.query.filter_by(id=id).delete()
        db.session.commit()
        flash("User deleted", "success")
    except:
        flash("There was an error deleting the user", "error")
        return redirect(f"/users/{id}")

    return redirect(f"/")

@app.route("/posts/<int:id>")
def show_post(id):
    """Display post details"""

    post = Post.query.get_or_404(id)
    return render_template("show_post.html", post=post)

@app.route("/users/<int:id>/posts/new")
def new_post_form(id):
    """Display new post form for user"""

    user = User.query.get_or_404(id)
    return render_template("add_post_form.html", user=user)

@app.route("/users/<int:id>/posts/new", methods=["POST"])
def add_post(id):
    """Create a new post in the databse"""

    title = request.form['title']
    content = request.form['content']
    user_id = id

    post = Post(title=title, content=content, user_id=user_id)
    
    try:
        db.session.add(post)
        db.session.commit()
        flash("New post added", "success")
    except:
        flash("There was an error adding the post", "error")

    return redirect(f"/posts/{post.id}")

@app.route("/posts/<int:id>/edit")
def edit_post_form(id):
    """Show form to edit post"""

    post = Post.query.get_or_404(id)
    return render_template("edit_post_form.html", post=post)

@app.route("/posts/<int:id>/edit", methods=["POST"])
def update_post(id):
    """Update post in the databse"""

    title = request.form['title']
    content = request.form['content']

    post = Post.query.get_or_404(id)
    post.title = title
    post.content = content

    try:
        db.session.add(post)
        db.session.commit()
        flash("This post has been updated", "success")
    except:
        flash("There was an error updating the post", "error")

    return redirect(f"/posts/{id}")

@app.route("/posts/<int:id>/delete", methods=["POST"])
def delete_post(id):
    """Delete post from database"""

    post = Post.query.get_or_404(id)
    
    try:
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        flash("Post deleted", "success")
    except:
        flash("There was an error deleting the post", "error")
        return redirect(f"/posts/{id}")

    return redirect(f"/users/{post.user_id}")
 