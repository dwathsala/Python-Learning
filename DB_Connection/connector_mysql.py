import mysql.connector

host = 'localhost'
database = 'sqldemo'
user = "root"
password = "12345"

query = "select * from users WHERE age=25;" #queries godak wenuwat ekam query eka update krnn puluwan 
query = "select * from users WHERE age=30;"
query = "DELETE FROM users WHERE age>28;"
query = "select * from users ;"
query = "update users set age=28 where name='kamal';"
query = "select * from users ;"
query = "show tables;"
query = "select * from users ;"
query = "drop table users;"
query = "show tables;"

try:
    connection = mysql.connector.connect(
        host = host, database = database, user = user, password = password)

    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()
    print(result)

    connection.commit()

except Exception as e:
    print("Something went wrong: ",e)


finally:
    if connection.is_connected():
        connection.close()
