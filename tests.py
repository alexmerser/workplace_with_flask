from flask.ext.testing import TestCase
from config import ROOT
import os
from apps import db, app
import unittest

class WorkplaceTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(ROOT, "test.db")
    TESTING = True

    test_user_data = {
        "email" : "test@workplace.is",
        "password" : "test",
        "first_name" : "First Name",
        "last_name" : "Last Name",
    }

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Testing Models
    def test_user_model(self):
        from apps.models import User
        # before creating, should have 0 user
        user_count = 0
        users = User.query.all()
        assert len(users) == user_count

        # create 1 user
        user = User(**self.test_user_data)
        db.session.add(user)
        db.session.commit()

        # now, should have 1 user
        users = User.query.all()
        assert len(users) == user_count+1

if __name__ == "__main__":
    unittest.main()
