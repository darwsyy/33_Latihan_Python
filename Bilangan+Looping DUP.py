import os
print(os.system("cls"))

print("<============ Program untuk menentukan GANJIL/GENAP ============>")

def ganjil_genap():
    while True:
        angka = int(input("Masukkan bilangan yang akan diperiksa: "))
        
        if angka % 2 == 0:
            print(angka, "adalah bilangan genap 🟢")
        else:
            print(angka, "adalah bilangan ganjil 🔴")
            
        if input("\nApakah ingin memeriksa bilangan lain? (Y/N):").upper() == "N":
            print("Terima kasih telah menggunakan program ini.")
            print("================================================================")
            break
        else:
            continue
    
ganjil_genap()