from flask import Flask, render_template


######

app = Flask(__name__)

######

@app.route("/")
def index():

    return render_template ("home.html.jinja")

    # return ("<p style=\"color:red;\">Hello!</p>")


######

@app.route("/Ping")
def ping():

    return ("<p style=\"color:green;\">Pong!</p>")

ping()

######

@app.route("/hello/<name>")
def hello(name):
    # return ("Hello" + name)
    return (f"Hello {name}")

@app.route("/testImg")
def testImg():
    return ("img src=\"https://s3.amazonaws.com/static.rogerebert.com/uploads/review/primary_image/reviews/reality-movie-review-2023/reality-movie-review-2023.jpeg\" alt=\"reality\"")
