from starter_code.models.item import ItemModel
from starter_code.tests.base_test import BaseTest
from starter_code.models.store import StoreModel


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            # add third store ID param
            StoreModel('test').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))
