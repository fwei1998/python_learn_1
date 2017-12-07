from flask import Flask
app = Flask(__name__)
app.run("localhost",port=8080)


@app.route('/')
def index():
    return "Hello World!"