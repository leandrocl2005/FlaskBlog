from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_dance.contrib.google import make_google_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

client_id = "PUT_HERE_YOUR_GOOGLE_CLIENT_ID"
client_secret = "PUT_HERE_YOUR_GOOGLE_CLIENT_SECRET"

google_blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    scope=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile"
    ],
    hosted_domain="localhost:5000",
    redirect_to="login"
)

app.register_blueprint(google_blueprint, url_prefix="/login", offline=True)

from app import routes, models
