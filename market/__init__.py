from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import flask_wtf
import os
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL') 
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SESSION_COOKIE_SECURE ']=False
#have the cookie sent by the flask app
app.config["SECURITY_CSRF_COOKIE"] = {"key": "csrf_token"}
app.config["WTF_CSRF_TIME_LIMIT"] = None # Don't have csrf tokens expire (they are invalid after logout)
# You can't get the cookie until you are logged in.
app.config["SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS"] = True
app.config['WTF_CSRF_ENABLED'] = False


# Enable CSRF protection
csrf=CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
flask_wtf.CSRFProtect(app)
migrate=Migrate(app,db)

# csrf_token=CsrfProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes