from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/emotion": {"origins": "http://localhost:3000"}}, supports_credentials=True)

from app import routes
