# Flask app main file
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Preventivatore RCA Online!'