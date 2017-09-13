from random import randint
from num2words import num2words
from easygui import *
import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

correctQ = 0
incorrectQ = 0
words = ""
number = 0
x = 0

def question():
    global words
    global number
    number = randint(1, 1000)
    words = num2words(number)


def main():
    global correctQ
    global incorrectQ
    question()
    userInput = enterbox(msg="Enter the number as an integer \n"+str(words), title="num2words")
    if int(userInput) == number:
        correctQ += 1
        msgbox(msg="Correct!")
        correct = True
        c.execute("""INSERT INTO results (question,answer,correct,studentID) 
                    VALUES(?,?,?,?)""",(words,userInput,correct,finalID))
        conn.commit()
    else:
        incorrectQ += 1
        msgbox(msg="Incorrect!")
        correct = False
        c.execute("""INSERT INTO results (question,answer,correct,studentID) 
                    VALUES(?,?,?,?)""",(words,userInput,correct,finalID))
        conn.commit()

def login():
    global finalID
    username = enterbox(msg="Please enter your username")
    c.execute("SELECT ID FROM student WHERE userName=?", (username,))
    rows = c.fetchall()
    studentID = rows[0]
    studentID = list(map(int, studentID))
    finalID = studentID[0]
    loop()


def loop():
    for x in range(0, 10):
        main()

    else:
        percent = (int(correctQ) / 10)*100
        msgbox(percent)



login()


