
from starter_code.models.user import UserModel
from starter_code.tests.base_test import  BaseTest


class UserTest(BaseTest):

    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password, 'abcd', 'Failed - Password does not match')




