import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods =["GET", "POST"])
def username():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.write(request.form["username"])
    return render_template("register.html")

@app.route('/play')
def play():
    data = []
    with open("data/players.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("play.html", players=data)

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/about')
def about():
    return render_template("about.html")

if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            