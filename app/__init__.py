from flask import Flask #imports flask
from config import Config #imports Config object

app = Flask(__name__) #creates a flask object with the name of the module it is used in
app.config.from_object(Config) #updates the values of app.config to that from the Config object


from app import routes #imports routes