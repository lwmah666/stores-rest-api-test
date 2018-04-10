
from starter_code.models.user import UserModel
from starter_code.tests.system.system_base_test import BaseTest
import json

class UserTest(BaseTest):

    def test_register_user(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                # data is converted into form data, not json
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully'},
                                     json.loads(response.data.decode('utf-8')))

    def test_register_and_login(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                # data is converted into form data, not json
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})

                # convert to bytes to string
                responseData = auth_response.data.decode('utf-8')
                # convert string to json and then get keys
                self.assertIn('access_token', json.loads(responseData).keys())

    def test_register_duplicate_user(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

            # should get a 400 error for second post
            self.assertEqual(response.status_code, 400)
            self.assertDictEqual({'message': 'A user with that username already exists'},
                                 json.loads(response.data.decode('utf-8')))
