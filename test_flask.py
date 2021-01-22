from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample user and Post."""

        Post.query.delete()
        User.query.delete()

        user = User(first_name="TestFirst", last_name="TestLast", image_url="https://i.pinimg.com/originals/45/a4/e1/45a4e1a9dcddbd936c5586419842e397.jpg")
        db.session.add(user)
        db.session.commit()

        post = Post(title="Test Post", content="Some Content...", user_id=user.id)
        db.session.add(post)
        db.session.commit()

        self.user_id = user.id
        self.post_id = post.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestFirst', html)
            self.assertIn('TestLast', html)

    def test_user_profile(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3">User Profile</h1>', html)
            self.assertIn('<h2>TestFirst TestLast</h2>', html)
            self.assertIn(f'<li><a href="/posts/{self.post_id}">Test Post</a></li>', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "TestFirst2", "last_name": "TestLast2", "image_url": ""}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3">User Profile</h1>', html)

    def test_edit_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3">Edit User</h1>', html)

    def test_add_post(self):
        with app.test_client() as client:
            d = {"title": "Test Title2", "content": "Content content"}
            resp = client.post(f"/users/{self.user_id}/posts/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3">Test Title2</h1>', html)

    def test_edit_post(self):
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3">Edit Post for TestFirst TestLast</h1>', html)
