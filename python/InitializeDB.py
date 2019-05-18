#sql file and python, followed this tutorial ->
#https://iotbytes.wordpress.com/sqlite-db-on-raspberry-pi/
import sqlite3

db_name = "mydb"

ex_this_file = "definition.sql"

definition = ""

with open(ex_this_file, 'r') as SchemaFile:
	definition = SchemaFile.read().replace('\n','')

conn = sqlite3.connect(db_name)
c = conn.cursor()

sqlite3.complete_statement(definition)
c.executescript(definition)

c.close()
conn.close()
