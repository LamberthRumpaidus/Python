import getpass
import random
import time


def register():
    username = input("Buat nama pengguna: ")
    password = getpass.getpass("Buat kata sandi: ")

    # Simpan nama pengguna dan kata sandi
    with open("user_data.txt", "w") as file:
        file.write("{}\n{}".format(username, password))


def login():
    username = input("Masukkan nama pengguna: ")
    password = getpass.getpass("Masukkan kata sandi: ")

    # Periksa apakah nama pengguna dan kata sandi benar
    with open("user_data.txt", "r") as file:
        correct_username, correct_password = file.read().split("\n")

    if username == correct_username and password == correct_password:
        return True
    else:
        return False


def reset_password():
    username = input("Masukkan nama pengguna: ")

    # Periksa apakah nama pengguna benar
    with open("user_data.txt", "r") as file:
        correct_username, _ = file.read().split("\n")

    if username == correct_username:
        new_password = getpass.getpass("Buat kata sandi baru: ")

        # Simpan nama pengguna dan kata sandi baru
        with open("user_data.txt", "w") as file:
            file.write("{}\n{}".format(username, new_password))
        print("Kata sandi berhasil direset!")
    else:
        print("Nama pengguna tidak ditemukan!")


def logout():
    return False


def game():
    levels = [10, 50, 100, 200, 500]
    score = 0

    for i, level in enumerate(levels):
        number = random.randint(1, level)
        guesses = 0
        print("Level {}: Tebak angka antara 1 dan {}".format(i+1, level))
        start_time = time.time()

        while True:
            guess = int(input("Masukkan tebakan Anda: "))
            guesses += 1

            if time.time() - start_time > 30:  # Batas waktu 30 detik
                print("Waktu habis! Anda tidak menebak angka dalam batas waktu.")
                break

            if guess < number:
                print("Terlalu rendah!")
            elif guess > number:
                print("Terlalu tinggi!")
            else:
                print("Selamat! Anda menebak angka dalam {} percobaan.".format(guesses))
                score += level // guesses  # Tambahkan poin ke skor
                break

    print("Skor akhir Anda adalah: ", score)

    # Simpan skor pemain ke file teks
    with open("leaderboard.txt", "a") as file:
        file.write("{}: {}\n".format(username, score))


def main():
    register()

    if login():
        print("Login berhasil!")
        game()

        if logout():
            print("Logout berhasil!")
        else:
            print("Logout gagal!")

        reset_password()

        # Tampilkan leaderboard
        print("\nLeaderboard:")
        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())

    else:
        print("Nama pengguna atau kata sandi salah!")


if __name__ == "__main__":
    main()
