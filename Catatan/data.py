import json

# Data mahasiswa Input Aktif
# def data_mahasiswa():
#     data_mahasiswa = []

#     while True:
#         npm = 100
#         if data_mahasiswa:
#             npm = max([siswa["npm"] for siswa in data_mahasiswa]) + 1
#         nama = input("Masukkan nama mahasiswa: ")
#         jurusan = input("Masukkan jurusan mahasiswa: ") 
        
#         data_mahasiswa.append({"npm": npm, "nama": nama, "jurusan": jurusan})
        
#         lagi = input("Apakah ingin menambahkan data lagi? (y/n): ")
#         if lagi.lower() != 'y':
#             break
#     return data_mahasiswa
# data_mahasiswa = data_mahasiswa()

# Data mahasiswa Input Pasif
data_mahasiswa = [
    {"npm": "101", "nama": "Tangguh", "jurusan": "TKJ"},
    {"npm": "102", "nama": "Darwisy", "jurusan": "TKJ"}
]

# 1. Menulis/Menyimpan List/Dict ke File JSON (dump)
with open("Operation/Catatan/data_siswa.json", "w") as file_json:
    json.dump(data_mahasiswa, file_json, indent=4)

# 2. Membaca File JSON kembali ke Python (load)
with open("Operation/Catatan/data_siswa.json", "r") as file_json:
    data_terbaca = json.load(file_json)

print("Data dari JSON:")
print(data_terbaca)