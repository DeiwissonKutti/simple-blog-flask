from flask import Flask, render_template, redirect
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'ano_atual': datetime.now().year}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)