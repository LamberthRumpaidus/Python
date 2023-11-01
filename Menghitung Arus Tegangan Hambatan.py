while True:
    try:
        print("===================================================================================================")
        print("Program Menghitung Tegangan (V), Arus (I), dan Hambatan (R) (Hukum Ohm) by LamberhPaulinusRumpaidus")
        print("===================================================================================================")
        print("Pilih yang ingin dihitung:")
        print("1. Tegangan (V)")
        print("2. Arus (I)")
        print("3. Hambatan (R)")
        pilihan = int(input("Silakan masukkan pilihan (1/2/3):"))

        if pilihan == 1:
            I = float(input("Masukkan Nilai Arus (I) dalam Ampere (A): "))
            R = float(input("Masukkan Nilai Hambatan (R) dalam Ohm (Ω): "))
            V = I * R
            print(f"Tegangan (V) = {V} Volt (V)")
        elif pilihan == 2:
            V = float(input("Masukkan Nilai Tegangan (V) dalam Volt (V): "))
            R = float(input("Masukkan Nilai Hambatan (R) dalam Ohm (Ω): "))
            I = V / R
            print(f"Arus (I) = {I} Ampere (A)")
        elif pilihan == 3:
            V = float(input("Masukkan Nilai Tegangan (V) dalam Volt (V): "))
            I = float(input("Masukkan Nilai Arus (I) dalam Ampere (A): "))
            R = V / I
            print(f"Hambatan (R) = {R} Ohm (Ω)")
        else:
            print("Pilihan tidak valid.")
            continue

        pilih = input("Apakah Anda masih ingin menggunakan program? (Y/N): ")
        if pilih.lower() == 'n':
            print("Terima Kasih Telah Menggunakan Program")
            break
        elif pilih.lower() != 'y':
            print("Silakan Input yang benar")
    except ValueError:
        print("Silakan masukkan pilihan yang valid.")
