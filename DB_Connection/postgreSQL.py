import psycopg2

HOST = "localhost"
DBNAME = "sqldemo"
USER = "postgres"
PASSWORD = "12345"
PORT = "5432"

query = "CREATE TABLE users (name VARCHAR(20), age INT);"
query = "INSERT INTO users VALUES ('kamal', 20),('Saman',33),('Nimali' , 25) ;"
query = "SELECT *FROM users;"
query = "SELECT *FROM users WHERE age>20;"
query = "DELETE FROM users WHERE name='kamal';"
query = "SELECT *FROM users;"

query = "UPDATe users SET age=40 WHERE name = 'Saman';"
query = "SELECT *FROM users;"

query = "DROP TABLE users;"

connection = None
cursor = None

try:
    connection = psycopg2.connect(host = HOST, dbname = DBNAME, user = USER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()
    cursor.execute(query)

    '''result = cursor.fetchall()   #use to dispaly data in terminal
    print(result)'''

    connection.commit()  #To commit database changes

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    connection.close()