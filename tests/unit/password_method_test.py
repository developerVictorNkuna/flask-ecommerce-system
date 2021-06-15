from unittest import TestCase
from market.models import User
from tests.base_test import  BaseTest

class PasswordMethodTest(BasTest):
    def test_password_method(self):
        # test password method works as expected
        password_user = User(id=1, username='Kate', email_address='kate@gmail.com', password_hash='#&*565&*&&^489846&*^%%$', budget=200000).password
        # self.assertEqual(password_user.password_hash, '#&*565&*&&^489846&*^%%$')
        # print(password_user)
        self.assertEqual(password_user.password_hash, '#&*565&*&&^489846&*^%%$')
        