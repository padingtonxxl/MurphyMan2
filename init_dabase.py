import sqlite3

ini_file = open("murphyman2.ini", 'r')
fileLines = ini_file.readlines()
database_name = ""
for line in fileLines:
    splits = line.split( '=')
    parameter = splits[0]
    value = splits[1].rstrip('\n')
    if parameter == "database.name":
        database_name = value

if database_name == "":
    database_name = "murphyman2"

database_filename = database_name + ".db"

database_file = open(database_filename, 'w')
database_file.close()

conn = sqlite3.connect(database_filename)

#Table creation
conn.execute("CREATE TABLE config (parameter text, value text)")
print("Table 'config' created")
conn.execute("CREATE TABLE players (id integer, name text, points integer )")
print("Table 'players' created")

#Table filling
params = (database_name,)
conn.execute("INSERT INTO config values ('database.name',?)", params)
params = (database_filename,)
conn.execute("INSERT INTO config values ('database.filename',?)", params)

for row in conn.execute('SELECT * FROM config'):
    print(row)

conn.commit()
conn.close()