from flask import Flask , render_template , url_for

app = Flask(__name__)
print(__name__)

@app.route("/index.html")
def my_home():
    return  render_template('index.html')

@app.route("/about.html")
def about():
    return  render_template('about.html')

@app.route("/works.html")
def work():
    return  render_template('works.html')

@app.route("/work.html")
def work1():
    return  render_template('work.html')

@app.route("/contact.html")
def contact():
    return  render_template('contact.html')
