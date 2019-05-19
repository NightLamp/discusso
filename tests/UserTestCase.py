import unittest, os
from app import app, db
from app.models import Users, Posts, Replies

class UserTestCase(unittest.TestCase):

    def setup(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config[SQLALCHEMY_DATABASE_URI]= \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        user1 = User(username="a",email="a@test.com") 
        #user1.set_password("a")
        user1.admin = False

        user2 = User(username="b",email="b@test.com")
        #user2.set_password("b")
        user2.admin = False

        Post1 = Post(title="test1", desc="t1", user_id=user1.id)
        Reply1 = Reply(post_id=Post1.id, test="reply", stance=True,
                       user_id=user2.id)

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(Post1)
        db.session.add(Reply1)
        db.session.commit()

    def tearDown(self):
        db.seesion.remove()
        db.drop_all()

    def test_password_hashing(self):
        user = User.query.get(0)
        user.set_password('example')
        self.assertFalse(user.check_password('close'))
        self.assertTrue(user.check_password('example'))

    def test_db_commit(self):
        pass

    def test_update_bio(self):
        pass

    def test_post_delete(self):
        pass
    def test_reply_delete(self):
        pass
    
