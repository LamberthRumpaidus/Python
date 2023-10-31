import turtle


def draw_rose():
    window = turtle.Screen()
    window.bgcolor("white")
    rose = turtle.Turtle()
    rose.shape("turtle")
    rose.speed(10)

    rose.color("red")  # Warna bunga mawar merah
    for _ in range(36):  # Menggambar bunga mawar
        draw_petal(rose)
        rose.right(10)

    rose.color("green")
    rose.right(90)
    rose.forward(300)  # Menggambar batang

    window.exitonclick()


def draw_petal(turtle):
    for _ in range(2):  # Menggambar kelopak
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)


draw_rose()
