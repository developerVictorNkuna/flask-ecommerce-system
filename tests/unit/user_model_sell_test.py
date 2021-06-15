
#  THIS SHOULD BE AN INTEGRATION TEST












# import sys
# sys.path.append('C:/Code/FlaskEcom/market')
# from unittest import TestCase
# from market.models import User ,Item


# class UserModelSellTest(TestCase):
#     test_user_sell = User(
#         id=3,
#         username="Vincent Mapoulo",
#         email_address="vincentmapoulo@yahoo.com",
#         password_hash="monyati_tarven",
#         budget=7000

#     )
#     test_user_sell_item = Item(
#         id=3,
#         name="MacBook Pro",
#         price=15000,
#         barcode="######Mac&Tosh######",
#         description="Apple Laptop ,machine preinstalled with iStore Applications such as Safari,.."


#     )

#     def test_user_sell(self,item_object):
#         """
#         this function assert that the  test user can sell the...
#         ... item on the platform
#         and the sold item is created from Item class....
#         ... found in our tables/models
#         """
#         self.assertIn(self.test_user_sell_item in self.items)
# # if __name__ == '__main__':
# #     import UserModelSellTest
# #     UserModelSellTest.run()