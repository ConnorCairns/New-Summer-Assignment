import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()

def addItem():
    name = input("Please enter your full name: ")
    userName = input("Please enter your username: ")
    c.execute("""INSERT INTO student 
                (name,userName)values(?,?)""",
                (name,userName,)) #putting items into the database
    conn.commit() #commiting the changes

addItem()