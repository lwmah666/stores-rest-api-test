"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from starter_code.app import app
from starter_code.db import db


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Executes once per class for every test file
        :return:
        '''
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        db.init_app(app)

    def setUp(self):
        # Make sure database exists - executes for each test method

        with app.app_context():
            db.create_all()

        # Get a new test client for each test
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
