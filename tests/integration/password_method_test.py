from tests.base_test import BaseTest, db
from market.models import User

class PasswordMethodTest(BaseTest):
    def test_password_method(self):
        # test password method works as expected
        new_user = User(id=1, username='Kate', email_address='kate@gmail.com', password_hash='#&*565&*&&^489846&*^%%$', budget=200000)

        # save to db
        db.session.add(new_user)
        db.session.commit()

        # get user from db
        db_user = db.session.query(User).filter_by(email_address='kate@gmail.com').first()
        password = db_user.password
        print(password)

        
        
        