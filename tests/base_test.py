from unittest import TestCase

from market import app
from market   import db
import os


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
        app.config['WTF_CSRF_ENABLED']=False   #to disable csrf_token error
        
        with app.app_context():
            db.init_app(app)

    def setUp(self):
        with app.app_context():
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
