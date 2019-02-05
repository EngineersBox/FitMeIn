import mysql.connector
import SelfMethods

shopdb = mysql.connector.connect(host="localhost", user="root", password="Enderman0", auth_plugin='mysql_native_password', database="shopdatabase")
coffeedb = mysql.connector.connect(host="localhost", user="root", password="Enderman0", auth_plugin="mysql_native_password", database="coffeeshop")

print(shopdb)

dbcursor = shopdb.cursor()
coffeecursor = coffeedb.cursor()

class db_method:

    def addtable(name, type, location, services, timetable):

        sql = "SELECT rowid FROM components WHERE name = %s"
        val = (str(name),)
        dbcursor.execute(sql, val)
        data = dbcursor.fetchall()

        if len(data) == 0:
            dbcursor.execute("CREATE TABLE shops (name VARCHAR(255), type VARCHAR(255), location VARCHAR(255), services VARCHAR(255), timetable VARCHAR(255))")
            sql = "INSERT INTO shops (name, type, location, services, timetable) VALUES (%s, %s, %s, %s, %s)"
            val = (str(name), str(type), str(location), str(services), str(timetable))

            dbcursor.execute(sql, val)
            shopdb.commit()

            print(dbcursor.rowcount, "Record Inserted")

        else:

            print("Record Already Exists")

    def addData(name, type, service, time):

        sql = "SELECT rowid FROM components WHERE name = %s"
        val = (str(name),)
        dbcursor.execute(sql, val)
        data = dbcursor.fetchall()

        if len(data) > 0:
            sql = "UPDATE shops SET timetable = %s WHERE time"

#sql = "INSERT INTO criteria (name, services, timetable) VALUES (%s, %s, %s)"
#val = ("Coffee Co", "[Latte, Mocha]", "[9,11,13,15,17]")

#coffeecursor.execute(sql, val)
#coffeedb.commit()

#dbcursor.execute("CREATE TABLE shops (name VARCHAR(255), type VARCHAR(255), location VARCHAR(255), services VARCHAR(255), timetable VARCHAR(255))")
#sql = "INSERT INTO shops (name, type, location, services, timetable) VALUES (%s, %s, %s, %s, %s)"
#val = (str(name), str(type), str(location), str(services), str(timetable))

#dbcursor.execute(sql, val)

#shopdb.commit()
#print(dbcursor.rowcount, "Record Inserted")

#dbcursor.execute("SELECT * FROM shops WHERE timetable = '[9,11,13,15,17]'")

#result = dbcursor.fetchall()

for x in result:
    print(x)

#dbcursor.execute("SHOW TABLES")

#for x in dbcursor:
#    print(x)
#https://www.w3schools.com/python/python_mysql_where.asp
