import turtle
num = int(input("please input the number of line:"))

turtle.width(1)
turtle.speed(100)

for i in range(0,num+1):
    turtle.goto(i*20, 0)
    turtle.pendown()
    turtle.goto(i*20,(num)*20)
    turtle.penup()
    turtle.goto(0,i*20)
    turtle.pendown()
    turtle.goto((num)*20,i*20)
    turtle.penup()
    i += 1

turtle.done()