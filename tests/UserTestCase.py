import unittest, os
from app import app, db
from app.models import Users, Posts, Replies

class UserTestCase(unittest.TestCase):

    def setup(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config[SQLALCHEMY_DATABASE_URI]= \ 
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        user1 = 
        user2 =
        Post1 =
        Reply 1 =

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(Post1)
        db.session.add(Reply1)
        db.session.commit()

    def tearDown(self):
        db.seesion.remove()
        db.drop_all()

    def test_password_hashing(self):
        user = User.query.get()'put number here'
        user.set_password('example')
        self.assertFalse(user.check_password('close'))
        self.assertTrue(user.check_password('example'))

    def test_db_commit(self):

    def test_update_bio(self):

    def test_post_delete(self):

    def test_reply_delete(self):

    