from flask import Flask
app = Flask(__name__)

@app.route("/") #function decorator, acts as server
def hello():
	return "Hello World!"
