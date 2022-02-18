import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pineapple objectively does not belong on pizza'

from app import views

