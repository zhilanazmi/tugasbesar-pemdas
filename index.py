import mysql.connector

def db_config():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tubespemdas"
    )

# ---------------------------------------------
# Menampilkan halaman dashboard 

def home():
    print("Selamat datang di Toko Bangunan")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Pilih opsi (1/2/3): ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit_program()
    else:
        print("Opsi tidak valid. Silakan pilih lagi.")
        home()
# Fungsi untuk login
def login():
    # Implementasikan logika login di sini
    print("== Halaman Login ==")
    username = input("Username: ")
    password = input("Password: ")

    # Cek apakah user adalah admin atau user biasa (role)
    role = check_login(username, password)

    if role == "admin":
        admin_page()
    elif role == "user":
        user_page()
    else:
        print("Login gagal. Coba lagi.")
        login()

# Fungsi untuk register
def register():
    # Implementasikan logika register di sini
    print("== Halaman Register ==")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    # Implementasikan penyimpanan data register ke database
    save_register(username, password, email)

    print("Registrasi berhasil. Silakan login.")
    login()

# Fungsi untuk keluar dari program
def exit_program():
    print("Terima kasih! Program telah keluar.")
    exit()

# Fungsi untuk cek login dan mengembalikan role (user atau admin)
def check_login(username, password):
    conn = db_config()
    cursor = conn.cursor()
    query = "SELECT role FROM Login WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

# Fungsi untuk menyimpan data register ke database
def save_register(username, password, email):
    conn = db_config()
    cursor = conn.cursor()
    query = "INSERT INTO Login (username, password, role, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (username, password, 'user', email))
    conn.commit()
    conn.close()

# Fungsi untuk halaman admin
def admin_page():
    # Implementasikan halaman admin di sini
    print("== Halaman Admin ==")
    # Tambahkan menu untuk CRUD barang dan melihat data user

# Fungsi untuk halaman user
def user_page():
    while True:
        print("== Halaman User ==")
        print("1. Lihat Barang")
        print("2. Pembelian")
        print("3. Histori Transaksi")
        print("4. Logout")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            view_items()
        elif choice == "2":
            purchase()
        elif choice == "3":
            transaction_history()
        elif choice == "4":
            print("Anda telah logout.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

# Fungsi untuk melihat daftar barang
def view_items():
    # Implementasikan logika untuk menampilkan barang dari database
    print("== Daftar Barang ==")

# Fungsi untuk melakukan pembelian barang
def purchase():
    # Implementasikan logika pembelian barang
    print("== Pembelian Barang ==")

# Fungsi untuk melihat histori transaksi
def transaction_history():
    # Implementasikan logika untuk melihat histori transaksi
    print("== Histori Transaksi ==")

def main():
    while True:
        home()

if __name__ == "__main__":
    main()
