import mysql.connector

def db_config():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tubespemdas"
    )

# ---------------------------------------------

def create_user(username, password, role, email):
    connection = db_config()
    cursor = connection.cursor()
    query = "INSERT INTO Login (username, password, role, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (username, password, role, email))
    connection.commit()
    connection.close()

# Contoh fungsi untuk membaca data
def read_users():
    connection = db_config()
    cursor = connection.cursor()
    query = "SELECT * FROM Login"
    cursor.execute(query)
    for row in cursor:
        print(row)
    connection.close()

# Contoh pemanggilan fungsi
create_user('testuser', 'password123', 'user', 'test@test.com')
read_users()

