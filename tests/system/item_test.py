
from starter_code.models.store import StoreModel
from starter_code.models.item import ItemModel
from starter_code.models.user import UserModel
from starter_code.tests.base_test import BaseTest
import json


class ItemTest(BaseTest):

    # def setUp(self):
    #     super(ItemTest,self).setUp()
    #     with self.app as client:
    #         # to access the db
    #         with self.app_context():
    #             UserModel('test', '1234').save_to_db()
    #             # auth_request = client.post('/auth',
    #             #                            data=json.dumps({'username': 'test', 'password': '1234'}),
    #             #                            headers={'Content-Type': 'application/json'})
    #             # # self.assertEqual(auth_request.status_code, 200)
    #             #
    #             # self.auth_token = json.loads(auth_request.data.decode('utf-8'))['access_token']
    #             # self.access_token = {'Authorization': 'JWT ' + auth_token}
    #
    #             # data is converted into form data, not json
    #             client.post('/register', data={'username': 'test', 'password': '1234'})
    #             auth_response = client.post('/auth',
    #                                        data=json.dumps({'username': 'test', 'password': '1234'}),
    #                                        headers={'Content-Type': 'application/json'})
    #
    #             # convert to bytes to string
    #             # responseData = auth_response.data.decode('utf-8')
    #             token = json.loads(auth_response.data.decode('utf-8'))['access_token']
    #             self.access_token = {'Authorization': 'JWT ' + token}
    #             # convert string to json and then get keys
    #             # self.assertIn('access_token', json.loads(responseData).keys())

    def test_get_item_no_auth(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                response = client.get('/item/testItem')

                # no jwt authorization header - not logged in
                # ??? DOES NOT WORK!!
                self.assertEqual(response.status_code, 401)
                # self.assertIsNotNone(StoreModel.find_by_name(StoreTest.store))
                # self.assertDictEqual({'items': [], 'name': 'Superstore'},
                #                      json.loads(response.data.decode('utf-8')))

    def test_get_item_not_found(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})

                self.assertEqual(auth_response.status_code, 200)

                token = json.loads(auth_response.data.decode('utf-8'))['access_token']
                headers = {'Authorization': 'JWT ' + token}
                response = client.get('/item/testItem', headers=headers)

                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        pass

    def test_delete_item(self):
        pass

    def test_create_item(self):
        pass

    def test_create_duplicate_item(self):
        pass

    def test_put_item(self):
        pass

    def test_put_update_item(self):
        pass

    def test_item_list(self):
        pass


