#This only needs to be run once
import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""CREATE TABLE student
             (ID INTEGER,
              name TEXT,
              userName TEXT,
              PRIMARY KEY(ID))""")
conn.commit()
c.execute("""CREATE TABLE results
             (ID INTEGER,
              response TEXT,
              result BOOLEAN,
              PRIMARY KEY(ID))""")
conn.commit()

print("tbl has successfully been created... please close this window")
