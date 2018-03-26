from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "Index Page"

@app.route('/hello/')
def hello():
    return "hello world"

@app.route('/post/<string:author>/')
def show_outline(author):
    return author
