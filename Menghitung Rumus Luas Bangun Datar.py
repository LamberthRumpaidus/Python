import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    clear_screen()
    print("====================================================================")
    print("  Program Menghitung Luas Bangun Datar by LamberthPaulinusRumpaidus")
    print("====================================================================")
    print("Pilih bangun datar yang ingin dihitung luasnya:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Trapesium")
    print("5. Jajar Genjang")
    print("6. Belah Ketupat")
    print("7. Layang Layang")
    print("8. Lingkaran")

    try:
        pilihan = int(input("Silakan masukkan pilihan (1-8): "))
        Luas = 0

        if pilihan == 1:
            Sisi = float(input("Masukkan Panjang Sisi: "))
            Luas = Sisi * Sisi
        elif pilihan == 2:
            Panjang = float(input("Masukkan Panjang: "))
            Lebar = float(input("Masukkan Lebar: "))
            Luas = Panjang * Lebar
        elif pilihan == 3:
            Alas = float(input("Masukkan Alas: "))
            Tinggi = float(input("Masukkan Tinggi: "))
            Luas = 0.5 * Alas * Tinggi
        elif pilihan == 4:
            SisiAtas = float(input("Masukkan Panjang Sisi Atas: "))
            SisiBawah = float(input("Masukkan Panjang Sisi Bawah: "))
            Tinggi = float(input("Masukkan Tinggi: "))
            Luas = 0.5 * (SisiAtas + SisiBawah) * Tinggi
        elif pilihan == 5:
            Alas = float(input("Masukkan Alas: "))
            Tinggi = float(input("Masukkan Tinggi: "))
            Luas = Alas * Tinggi
        elif pilihan == 6 or pilihan == 7:
            Diagonal1 = float(input("Masukkan Panjang Diagonal 1: "))
            Diagonal2 = float(input("Masukkan Panjang Diagonal 2: "))
            Luas = 0.5 * Diagonal1 * Diagonal2
        elif pilihan == 8:
            JariJari = float(input("Masukkan Jari-Jari Lingkaran: "))
            Luas = 3.14159265359 * JariJari**2
        else:
            print("Pilihan tidak valid.")
            continue

        print(f"Luas adalah: {Luas}")

        Pilih = input("Apakah Anda masih ingin menggunakan program? (Y/N): ")
        if Pilih.lower() == 'n':
            print("Terima Kasih Telah Menggunakan Program")
            break
        elif Pilih.lower() != 'y':
            clear_screen()
            print("Silakan Input yang benar")
    except ValueError:
        print("Silakan masukkan pilihan yang valid.")
