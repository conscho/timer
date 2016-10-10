from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def timer():
    return str(time.time() * 1000)
