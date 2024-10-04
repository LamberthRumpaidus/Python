import turtle

# Fungsi untuk menggambar petal


def draw_petal(radius, angle):
    turtle.circle(radius, angle)
    turtle.left(180 - angle)
    turtle.circle(radius, angle)
    turtle.left(180 - (360 / 6))

# Fungsi untuk menggambar bunga mawar


def draw_rose(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    turtle.begin_fill()
    for _ in range(36):
        draw_petal(50, 60)
    turtle.end_fill()

# Fungsi untuk menggambar bunga matahari


def draw_sunflower(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    turtle.begin_fill()
    for _ in range(12):
        draw_petal(100, 40)
    turtle.end_fill()

    # Gambar pusat bunga
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

# Fungsi untuk menggambar bunga tulip


def draw_tulip(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    turtle.begin_fill()
    turtle.setheading(90)
    for _ in range(2):
        turtle.circle(50, 60)
        turtle.left(120)
        turtle.circle(50, 60)
        turtle.left(120)
    turtle.end_fill()

# Fungsi untuk menggambar bunga lilac


def draw_lilac(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    for _ in range(6):
        turtle.begin_fill()
        turtle.circle(30, 180)
        turtle.left(120)
        turtle.circle(30, 180)
        turtle.left(120)
        turtle.end_fill()
    turtle.right(60)

# Fungsi untuk menggambar bunga daisy


def draw_daisy(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    for _ in range(12):
        turtle.begin_fill()
        draw_petal(30, 60)
        turtle.end_fill()
        turtle.left(30)
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

# Fungsi untuk menggambar bunga lavender


def draw_lavender(petal_color, fill_color):
    turtle.color(petal_color, fill_color)
    for _ in range(8):
        turtle.begin_fill()
        turtle.circle(20, 180)
        turtle.left(120)
        turtle.circle(20, 180)
        turtle.left(120)
        turtle.end_fill()
    turtle.right(45)


# Daftar bunga yang dapat dipilih
flowers = [
    draw_rose,
    draw_sunflower,
    draw_tulip,
    draw_lilac,
    draw_daisy,
    draw_lavender,
]

# Fungsi untuk menggambar batang


def draw_stem():
    turtle.color("green")
    turtle.right(90)
    turtle.forward(200)

# Fungsi utama


def main(flower_choice, petal_color, fill_color):
    turtle.speed(10)
    turtle.bgcolor("lightblue")

    # Menggambar bunga berdasarkan pilihan
    # Memanggil fungsi bunga sesuai pilihan
    flowers[flower_choice](petal_color, fill_color)
    draw_stem()

    turtle.done()


if __name__ == "__main__":
    print("Selamat datang di program menggambar bunga!")
    while True:
        try:
            print("\nPilih bunga (0-5):")
            print("0: Mawar")
            print("1: Bunga Matahari")
            print("2: Tulip")
            print("3: Lilac")
            print("4: Daisy")
            print("5: Lavender")

            flower_choice = int(input("Masukkan pilihan Anda: "))
            if 0 <= flower_choice < len(flowers):
                break
            else:
                print("Pilihan bunga tidak valid! Silakan pilih angka antara 0 dan 5.")
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")

    # Meminta pengguna memilih warna
    petal_color = input(
        "Masukkan warna petal (contoh: 'red', 'yellow', 'blue', 'purple'): ").strip()
    fill_color = input(
        "Masukkan warna isi (contoh: 'pink', 'gold', 'lightgreen', 'lavender'): ").strip()

    # Meminta masukan sandi
    password = input("Masukkan sandi untuk menjalankan program: ")
    if password == "lam":
        main(flower_choice, petal_color, fill_color)
    else:
        print("Sandi salah! Program tidak dapat dijalankan.")
