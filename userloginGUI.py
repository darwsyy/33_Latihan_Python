import tkinter as tk
from tkinter import messagebox
import mysql.connector

# --- KONFIGURASI DATABASE ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="Darwisy030210",  
        database="app_db"
    )

# --- FUNGSI LOGIKA LOG IN & REGISTER ---
def register_user():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!")
        return

    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        
        messagebox.showinfo("Sukses", "Registrasi berhasil! Silakan login.")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("Gagal", f"Gagal mendaftar: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def login_user():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Peringatan", "Isi username dan password terlebih dahulu!")
        return

    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Berhasil", f"Login Berhasil!\nSelamat datang, {username}.")
            show_main_app_screen(username)
        else:
            messagebox.showerror("Gagal", "Username atau Password salah!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error Database", f"Koneksi gagal: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

# --- HALAMAN UTAMA SETELAH LOGIN ---
def show_main_app_screen(username):
    # Sembunyikan jendela login
    root.withdraw()

    # Buat jendela baru untuk aplikasi utama
    app_window = tk.Toplevel()
    app_window.title("Dashboard Aplikasi")
    app_window.geometry("400x300")

    tk.Label(app_window, text=f"Halo, {username}!", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(app_window, text="Kamu berhasil masuk ke dalam sistem.", font=("Arial", 10)).pack(pady=10)

    def logout():
        app_window.destroy()
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        root.deiconify() # Tampilkan kembali jendela login

    tk.Button(app_window, text="Logout", command=logout, bg="#d9534f", fg="white", font=("Arial", 10, "bold")).pack(pady=30)

# --- DESAIN TAMPILAN GUI (TKINTER) ---
root = tk.Tk()
root.title("Sistem Autentikasi User")
root.geometry("350x300")
root.resizable(False, False)

# Judul Form
lbl_title = tk.Label(root, text="Autentikasi User", font=("Arial", 14, "bold"))
lbl_title.pack(pady=15)

# Input Username
lbl_user = tk.Label(root, text="Username:", font=("Arial", 10))
lbl_user.pack(anchor="w", padx=40)
entry_username = tk.Entry(root, font=("Arial", 10), width=30)
entry_username.pack(padx=40, pady=(0, 10))

# Input Password
lbl_pass = tk.Label(root, text="Password:", font=("Arial", 10))
lbl_pass.pack(anchor="w", padx=40)
entry_password = tk.Entry(root, font=("Arial", 10), width=30, show="*")
entry_password.pack(padx=40, pady=(0, 15))

# Frame Tombol Action
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_login = tk.Button(btn_frame, text="Login", command=login_user, bg="#4CAF50", fg="white", width=12, font=("Arial", 10, "bold"))
btn_login.grid(row=0, column=0, padx=5)

btn_register = tk.Button(btn_frame, text="Register", command=register_user, bg="#2196F3", fg="white", width=12, font=("Arial", 10, "bold"))
btn_register.grid(row=0, column=1, padx=5)

# Jalankan Loop GUI
root.mainloop()