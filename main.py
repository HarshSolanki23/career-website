from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
  return "<h1>Hello world!<h1>"


@app.route("/careers/")
def careers():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
