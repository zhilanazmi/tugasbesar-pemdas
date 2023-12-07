import mysql.connector

db_config = {
    'host': 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'tubespemdas'
}

# Connect to database
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Database connected")

except Error as e:
    print(f"Error while connecting to MySQL {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Database disconnected")
