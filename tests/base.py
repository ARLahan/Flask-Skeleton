# tests/base.py


from flask.ext.testing import TestCase

from project import app, db
from project.user.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(first_name='Test', last_name='app', email='test@admin.com',
                    password='admin_user')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
