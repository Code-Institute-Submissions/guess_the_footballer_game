import os
import json
import random
from flask import Flask, render_template, session, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"
app.secret_key = os.urandom(24)

def users():
    with open("data/users.txt", "r") as user_data:
        registered_users = user_data.read().splitlines()
        return registered_users
    
def generate_random_player():
    with open("data/players.json", "r") as players_data:
        players_list = json.load(players_data)["players"]
        random.shuffle(players_list)
        return players_list
        
def start_game():
    session['question_number'] = 1
    session['players'] = generate_random_player()
    session['score'] = 0
    return session['question_number'], session['players'], session['score']
        
def user_scores():
    with open("data/scores.json", "r") as score_data:
        data = json.load(score_data)
        return data
   
"""Routes"""

@app.route('/')
def index():
    if session:
        return redirect(url_for("play"))
    else:
        return render_template("index.html")
    
@app.route('/login', methods = ["GET", "POST"])
def login():
    if session:
        return redirect(url_for("play"))
    else:
        if request.method == "POST":
            returning_user = request.form["username"]
            registered_users = users()
            if returning_user in registered_users:
                session['user'] = returning_user
                return redirect(url_for("play"))
            else:
                flash('The username "{}" is not recognized. Please register '.format(request.form["username"]))
        return render_template("login.html")

@app.route('/logout')
def logout():
        session.clear()
        return redirect(url_for("index"))
    
"""app.route('/register')
def register():
    if session:
        return redirect(url_for("play"))
    else:
        return render_template("register.html")
"""

@app.route('/register', methods = ["GET", "POST"])
def register_user():
    if session:
        return redirect(url_for("play"))
    else:
        if request.method == "POST":
            new_user = request.form["username"]
            registered_users = users()
            if new_user in registered_users:
                flash('The username "{}" is already taken. Please choose another'.format(request.form["username"]))
            else:
                if request.method == "POST":
                    user_list = open("data/users.txt", "a")
                    user_list.write(new_user + "\n")
                    session['user'] = new_user
                    return redirect(url_for("play"))
        return render_template("register.html")
    
@app.route('/play')
def play():
    if session:
        users()
        start_game()
        question_number = session['question_number']
        players = session['players']
        score = session['score']
        return render_template("play.html", question_number=question_number, players=players, score=score)
    else:
        return redirect(url_for("index"))
 
@app.route('/play', methods = ["POST"])
def answers():
    if session:
        players = session['players']
        if request.method == "POST":
            session['question_number'] +=1
            session['guess'] = request.form.get("user_answer").lower()
            session['correct_answer'] = request.form.get("answer")
            if session['guess'] == session['correct_answer']:
                session['score'] +=1
            return render_template("play.html", players=players, question_number=session['question_number'], guess=session['guess'], correct_answer=session['correct_answer'], score=session['score'])
    else:
        return redirect(url_for("index"))
      
@app.route('/scoreboard') 
def scoreboard():
    return render_template("scoreboard.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)