from num2words import num2words
from random import randint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    username = db.Column(db.String(100))

    def __init__(self, name, username):
        self.name = name
        self.username = username

x = 0

correct = 0
incorrect = 0

def question():
    global correct
    global incorrect
    number = randint(1, 1000)
    print(number)
    words = num2words(number)
    print(words)

    print("What is " + words + " as an integer number")
    x = input()
    
    if int(x) == number:
        print("Correct")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1

@app.route("/")
def home():

    return "Hello World"

if __name__ == "__main__":
    app.run()
"""
for x in range(0, 10):
    question()

else:
    print(correct)
    percent = (int(correct) / 10)*100
    print(percent)"""