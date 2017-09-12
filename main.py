from random import randint
from num2words import num2words
from easygui import *

correct = 0
incorrect = 0
words = ""
number = 0
x = 0

def question():
    global words
    global number
    number = randint(1, 1000)
    words = num2words(number)


def main():
    global correct
    global incorrect
    question()
    input = enterbox(msg="Enter the number as an integer \n"+str(words), title="num2words")
    if int(input) == number:
        correct += 1
        msgbox(msg="Correct!")
    else:
        incorrect += 1
        msgbox(msg="Incorrect!")


for x in range(0, 10):
    main()

else:
    percent = (int(correct) / 10)*100
    msgbox(percent)


