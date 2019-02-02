"""local database of python sqlite3"""

import sqlite3 as sql 

db = sql.connect('/home/rayuga/Desktop/mydatabase.db')

c = db.cursor()

c.execute('create table data(id int(5) primary key,name varchar(50))')

c.execute('insert into data values (1,"garvit"), (2,"Java"), (3,"python")')

db.commit()


