from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
bootstrap = Bootstrap(app)

from app import routes
