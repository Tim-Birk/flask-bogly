import datetime
from flask_sqlalchemy import SQLAlchemy
from pytz import timezone
tz = timezone('EST')

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50),
                     nullable=False)
    image_url = db.Column(db.String(),
                     nullable=False, default='https://t4.ftcdn.net/jpg/03/46/93/61/360_F_346936114_RaxE6OQogebgAWTalE1myseY1Hbb5qPM.jpg')

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User - id: {u.id},  name: {u.last_name}, {u.first_name}>"

    def get_full_name(self):
        """Return users full name"""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(),
                     nullable=False)
    content = db.Column(db.String(),
                     nullable=False)
    created_at = db.Column(db.DateTime,
                     nullable=False, default=datetime.datetime.now(tz))
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'))
    
    user = db.relationship( 'User', backref='posts')

    def __repr__(self):
        """Show info about post."""

        p = self
        return f"<Post - id: {p.id},  title: {p.title}>"
    
    def show_est_formatted_date(self):
        """Show a formatted date in Eastern time"""
        return self.created_at.strftime("%b %d %Y %I:%M:%S %p")