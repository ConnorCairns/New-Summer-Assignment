#This only needs to be run once
import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""CREATE TABLE student
             (ID INTEGER NOT NULL,
              name TEXT NOT NULL,
              userName TEXT NOT NULL,
              PRIMARY KEY(ID))""")
conn.commit()
c.execute("""CREATE TABLE results
             (ID INTEGER NOT NULL,
              question TEXT NOT NULL,
              answer TEXT NOT NULL,
              correct BOOLEAN NOT NULL,
              sessionID INTEGER NOT NULL,
              studentID INTEGER NOT NULL,
              FOREIGN KEY(studentID) REFERENCES student(ID) 
              PRIMARY KEY(ID))""")
conn.commit()

print("tbl has successfully been created... please close this window")
