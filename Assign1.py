# First Assignment
import uuid
import sqlite3
from datetime import datetime

con = sqlite3.connect('firstassign.db') 
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS basic
                (name text PRIMARY KEY, id decimal(7,2))''')

Id = uuid.uuid1().int
# (Id)[:8] 
Name = input("Enter your name: ")
datetime = datetime.now()

# print(f"Hello, {Name}\n Your Id number: {Id}\n Current date and time: {datetime}")
cur.execute('''INSERT OR IGNORE INTO basic 
VALUES(?, ?)''', (Name, Id))

con.commit()
print ( 'Data entered successfully.' )
con.close ()
if (con):
  con.close()
  print("\nThe SQLite connection is closed.")

