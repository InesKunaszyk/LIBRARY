from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# metoda from object wczytuje ustawienia dla aplikacji z danego obiektu!

from Book_Library import authors
