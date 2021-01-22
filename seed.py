"""Seed file to make sample data for blogly db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty them
User.query.delete()
Post.query.delete()

# Add users
tim = User(first_name='Tim', last_name='Kenney', image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/56649400_10103839445921552_8360508541538140160_o.jpg?_nc_cat=108&ccb=2&_nc_sid=09cbfe&_nc_ohc=0DtIqNDxcWUAX9DPHS3&_nc_ht=scontent-lga3-2.xx&oh=6b442d20b854446518da446bc822f850&oe=602F3F1E")
tom = User(first_name='Tom', last_name='Williams', image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/81803994_10220904051892445_4609389353385328640_n.jpg?_nc_cat=102&ccb=2&_nc_sid=09cbfe&_nc_ohc=iGnCcONdSsAAX-5OBQb&_nc_ht=scontent-lga3-2.xx&oh=5dd88579ada6c1be2a11934e5ae22c3c&oe=60305AB6")
steve = User(first_name='Steve', last_name='Michaels', image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/118516525_10218749769475569_1010548603550265978_n.jpg?_nc_cat=111&ccb=2&_nc_sid=09cbfe&_nc_ohc=10kacyMU5r4AX-G6Wt3&_nc_ht=scontent-lga3-2.xx&oh=0a9c74164842c57c164250c3a16cd0c1&oe=6030BF79")

# Add new objects to session, so they'll persist
db.session.add(tim)
db.session.add(tom)
db.session.add(steve)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add posts
post1 = Post(title='Test Post 1', content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=1)
post2 = Post(title='Test Post 2', content="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.", user_id=3)
post3 = Post(title='Test Post 3', content="Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?", user_id=2)
post4 = Post(title='Test Post 4', content="At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.", user_id=1)

# Add new objects to session, so they'll persist
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)

# Commit--otherwise, this never gets saved!
db.session.commit()

