import turtle as tu
screen=tu.Screen()
screen.setup(width=1000, height=600)
screen.title("My Turtle Window")
screen.bgpic('bgs.png')
pen=tu.Turtle()
pen.pensize(13)
pen.color('white')
pen.begin_fill()
pen.speed(5)
# E
pen.penup()
pen.goto(-450, 0)
pen.pendown()
pen.right(90)
pen.backward(150)
pen.left(90)
pen.forward(90)
pen.penup()
pen.goto(-450,0)
pen.pendown()
pen.forward(90)
pen.penup()
pen.goto(-450,75)
pen.pendown()
pen.forward(90)
# I
pen.penup()
pen.goto(-340,0)
pen.pendown()
pen.left(90)
pen.forward(50)
pen.penup()
pen.goto(-340,75)
pen.left(90)
pen.pensize(8)
pen.dot()
# d
pen.pensize(13)
pen.penup()
pen.goto(-285,75)
pen.pendown()
pen.circle(40)
pen.penup()
pen.goto(-245,0)
pen.pendown()
pen.left(-90)
pen.forward(150)
# M
pen.penup()
pen.goto(-150,0)
pen.pendown()
pen.setheading(90)
pen.forward(150)
pen.setheading(-65)
pen.forward(150)
pen.setheading(65)
pen.forward(150)
pen.setheading(-90)
pen.forward(150)
# u
pen.penup()
pen.goto(-9,78)
pen.pendown()
pen.setheading(-90)
pen.forward(50)
pen.circle(30,90)
pen.forward(10)
pen.circle(30,90)
pen.forward(50)
pen.backward(75)
# b
pen.penup()
pen.goto(75,150)
pen.pendown()
pen.setheading(-90)
pen.forward(110)
pen.circle(40)
# a
pen.penup()
pen.goto(168,40)
pen.pendown()
pen.circle(40)
pen.penup()
pen.goto(250,75)
pen.pendown()
pen.setheading(-90)
pen.forward(70)
# r
pen.penup()
pen.goto(265,75)
pen.pendown()
pen.forward(70)
pen.penup()
pen.backward(10)
pen.pendown()
pen.circle(100,-40)
# a
pen.penup()
pen.goto(300,65)
pen.pendown()
pen.circle(40)
pen.penup()
pen.goto(373,75)
pen.pendown()
pen.setheading(-90)
pen.forward(70)
# k
pen.penup()
pen.goto(387,155)
pen.pendown()
pen.setheading(-90)
pen.forward(150)
pen.penup()
pen.backward(35)
pen.pendown()
pen.setheading(-45)
pen.forward(50)
pen.penup()
pen.goto(387,40)
pen.pendown()
pen.setheading(45)
pen.forward(50)

pen.penup()
pen.pencolor('yellow')
pen.goto(-165,-200)
pen.write('YouTube | AK Deep Knowledge ',font=('Times New Roman',20))
pen.goto(-165,-225)
pen.write('Code is written by Arsalan Khatri',font=('Times New Roman',15))
pen.hideturtle()
# star
pen.pensize(3)
pen.color("yellow", "yellow")
pen.penup()
pen.goto(200, 250)
pen.pendown()
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()

pen.pensize(3)
pen.color("yellow", "yellow")
pen.penup()
pen.goto(250, 250)
pen.pendown()
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()

pen.pensize(3)
pen.color("yellow", "yellow")
pen.penup()
pen.goto(225, 215)
pen.pendown()
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()

pen.pensize(3)
pen.color("yellow", "yellow")
pen.penup()
pen.goto(200, -194)
pen.pendown()
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()

pen.pensize(3)
pen.color("yellow", "yellow")
pen.penup()
pen.goto(-206, -194)
pen.pendown()
pen.begin_fill()
for i in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()
tu.done()