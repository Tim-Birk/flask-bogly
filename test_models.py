from unittest import TestCase

from app import app
from models import db, User, Post
from datetime import datetime

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self):
        """Clean up any existing users."""

        Post.query.delete()
        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_get_full_name(self):
        user = User(first_name="TestFirstName", last_name="TestLastName")
        self.assertEquals(user.get_full_name(), "TestFirstName TestLastName")

    def test_show_est_formatted_date(self):
        post = Post(title="Test Title", content="Some Content...", created_at=datetime(2021, 1, 1, 9, 00))
        self.assertEquals(post.show_est_formatted_date(), "Jan 01 2021 09:00:00 AM")

    
