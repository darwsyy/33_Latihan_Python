import mysql.connector

# Konfigurasi Koneksi Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="Darwisy030210",
        database="app_db"
    )

# Fitur Register (Tambah User Baru)
def register():
    print("\n--- REGISTRASI USER BARU ---")
    username = input("Masukkan Username Baru: ")
    password = input("Masukkan Password Baru: ")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        
        print("Registrasi berhasil! Silakan login.")
    except mysql.connector.Error as err:
        print(f"Gagal mendaftar: {err}")
    finally:
        cursor.close()
        conn.close()

# Fitur Login
def login():
    print("\n--- LOGIN USER ---")
    username = input("Username: ")
    password = input("Password: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        print(f"\nLogin Berhasil! Selamat datang, {username}.")
        return True
    else:
        print("\nUsername atau password salah!")
        return False

# Menu Utama
def main():
    while True:
        print("\n=== MENU APLIKASI ===")
        print("1. Login")
        print("2. Register (Buat Akun)")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            if login():
                # Jalankan fungsi utama aplikasimu di sini setelah berhasil login
                print("\n[Aplikasi Utama Berjalan...]")
                break
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()