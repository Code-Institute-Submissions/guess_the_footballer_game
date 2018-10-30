import os
import json
import random
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods =["GET", "POST"])
def register():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            user_list.write(request.form["username"])
    if request.method == "POST":
        flash("Thanks for registering {}!".format(request.form["username"]))
    return render_template("register.html")

@app.route('/play')
def play():
    data = []
    with open("data/players.json", "r") as players_data:
        data = json.load(players_data)
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
            