import turtle

def draw_gap():
    turtle.penup()
    turtle.fd(5)

def draw_line(draw):
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(90)
    draw_gap()
    turtle.left(90)


def draw_digit(num):
    draw_line(True) if num in [2,3,4,5,6,8,9] else draw_line(False)
    draw_line(True) if num in [0,1,2,3,4,7,8,9] else draw_line(False)
    draw_line(True) if num in [0,2,3,5,6,7,8,9] else draw_line(False)
    draw_line(True) if num in [0,4,5,6,8,9] else draw_line(False)
    turtle.right(90)
    draw_line(True) if num in [0,2, 6, 8] else draw_line(False)
    draw_line(True) if num in [0,2,3,5, 6, 8, 9] else draw_line(False)
    draw_line(True) if num in [0,1,3,4,5, 6,7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(30)

def init():
    turtle.setup(1920, 1080, 0, 0)  # 设置画布大小 200 200 为屏幕位置
    turtle.speed()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.fd(-650)
    turtle.pensize(5)

def main():
    init()

    for i in range(0,10):
        if i in [0,3,6,9]:
            turtle.pencolor('red')
        elif i in [1,4,7]:
            turtle.pencolor('green')
        elif i in [2,5,8]:
            turtle.pencolor('blue')

        draw_digit(i)

main()

turtle.done()




