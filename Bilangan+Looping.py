import os
print(os.system("cls"))


def ganjil_genap():
    print("<============ Program untuk menentukan GANJIL/GENAP ============>\n")
    while True:
        angka = int(input("Masukkan bilangan yang akan diperiksa: "))
        
        if angka % 2 == 0:
            print(angka, "adalah bilangan genap 🟢")
        else:
            print(angka, "adalah bilangan ganjil 🔴")
            
        if input("\nApakah ingin memeriksa bilangan lain? (Y/N):").upper() == "N":
            print("Terima kasih telah menggunakan program ini.")
            print("================================================================\n")
            break
        else:
            continue


def prima():
    print("<============ Program untuk menentukan BILANGAN PRIMA ============>\n")
    while True:
        angka = int(input("Masukkan bilangan yang akan diperiksa: "))

        if angka < 2:
            print(angka, "bukan bilangan prima")
        else:
            prima = True

            for pembagi in range(2, int(angka ** 0.5) + 1):
                if angka % pembagi == 0:
                    prima = False
                    break

            if prima:
                print(angka, "adalah bilangan prima")
            else:
                print(angka, "bukan bilangan prima")

        if input("\nApakah ingin memeriksa bilangan lain? (Y/N): ").upper() == "N":
            print("Terima kasih telah menggunakan program ini.")
            print("================================================================\n")
            break


while True:
    program = input("Masukan Program yang ingin dijalankan\n Check Bilangan Prima = 1\n Check Bilangan Ganjil/Genap = 2\n Pilihan Anda: ")
    if program == "1":
        prima()
    elif program == "2":
        ganjil_genap()
    else:
        print("Program tidak dikenal.")
        break
