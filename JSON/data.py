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
    {"npm": "102", "nama": "Darwisy", "jurusan": "TKJ"},
    {"npm": "103", "nama": "Rizqie", "jurusan": "TKJ"},
    {"npm": "104", "nama": "Fahimma", "jurusan": "TKJ"},
    {"npm": "105", "nama": "Dafdil", "jurusan": "TKJ"},
    {"npm": "106", "nama": "Ohdan", "jurusan": "TKJ"}
]

with open("Operation/JSON/data_siswa.json", "w") as file_json:
    json.dump(data_mahasiswa, file_json, indent=4)

with open("Operation/JSON/data_siswa.json", "r") as file_json:
    data_terbaca = json.load(file_json)

print("Data dari JSON:")
while True:
    for siswa in data_terbaca:
        print(f"NPM: {siswa['npm']}, Nama: {siswa['nama']}, Jurusan: {siswa['jurusan']}")
    break
