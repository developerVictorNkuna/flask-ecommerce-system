import unittest
from unittest import TestCase
from market.models import User ,Item
from tests.base_test import BaseTest

class UserModelPurchaseTest(BaseTest):

    

    def test_user_purchase(self):
        test_user = User(id=2,
                username="Thabo",
                email_address="thabo@gmail.com",
                password_hash="vink4013",
                budget=7000)

        test_item = Item(id=2,
                name="Aduino-Rasberry-Pi",
                price=2500,
                barcode="******coode****",
                description="Mini computer for micro controller,and personal Iot Project",
                )

        can_buy = test_user.can_purchase(test_item)
        self.assertTrue(can_buy)

