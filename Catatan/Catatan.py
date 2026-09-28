
with open("Operation/Catatan/Informasi.txt", "w") as file:
    file.write("Halo, ini contoh tulisan ke informasi.txt.\n")
    file.write("Baris kedua data.\n")


with open("Operation/Catatan/Informasi.txt", "r") as file:
    isi_file = file.read()
    print("Isi file informasi.txt:")
    print(isi_file)