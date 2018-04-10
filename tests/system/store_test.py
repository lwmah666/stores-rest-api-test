
from starter_code.models.store import StoreModel
from starter_code.models.item import ItemModel
from starter_code.tests.base_test import BaseTest
import json


class StoreTest(BaseTest):

    store = 'Superstore'

    def test_create_store(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                # client.delete('Superstore')
                response = client.post('/store/' + StoreTest.store)

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name(StoreTest.store))
                self.assertDictEqual({'items': [], 'name': 'Superstore'},
                                     json.loads(response.data.decode('utf-8')))

    def test_create_duplicate_store(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                response = client.post('/store/Superstore')

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({'message': "A store with name 'Superstore' already exists."},
                                     json.loads(response.data.decode('utf-8')))

    def test_delete_store(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                # create the store and then delete it
                StoreModel('Superstore').save_to_db()
                response = client.delete('/store/Superstore')

                self.assertEqual(response.status_code, 200)
                self.assertEqual({'message': 'Store deleted'}, json.loads(response.data.decode('utf-8')))

    def test_find_store(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                StoreModel('Superstore').save_to_db()
                response = client.get('/store/Superstore')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'items': [], 'name': 'Superstore'},
                                     json.loads(response.data.decode('utf-8')))

    def test_store_not_found(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                response = client.get('/store/Superstore')

                self.assertEqual(response.status_code, 404)

                # normallly, don't have to check this for 404 errors
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(response.data.decode('utf-8')))

    def test_store_found_with_items(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('testItem', 19.99, 1).save_to_db()

                response = client.get('/store/test')
                self.assertEqual(response.status_code, 200)                                     
                self.assertDictEqual({'name': 'test', 'items': [{'name': 'testItem', 'price': 19.99 }]},
                                     json.loads(response.data.decode('utf-8'))) 

    def test_store_list(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                response = client.get('/stores')

                self.assertDictEqual({'stores': []},
                                     json.loads(response.data.decode('utf-8')))

                # {'stores': [store.json() for store in StoreModel.query.all()]}

    def test_store_list_with_items(self):
        with self.app as client:
            # to access the db
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('testItem', 19.99, 1).save_to_db()                     

                response = client.get('/stores')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'stores': [{'name': 'test', 'items': [{'name': 'testItem', 'price': 19.99 }]}]},
                                     json.loads(response.data.decode('utf-8')))