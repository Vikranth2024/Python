import turtle

t = turtle.Turtle()

t.speed(20)

t.penup()
t.goto(-100,0)
t.pendown()

#V
t.left(120)
t.forward(50)
t.backward(50)
t.right(60)
t.forward(50)

t.penup()
t.goto(-60,0)
t.pendown()

#I
t.left(30)
t.forward(40)
t.right(90)
t.forward(13)
t.backward(26)
t.forward(13)
t.right(90)
t.forward(40)
t.right(90)
t.forward(13)
t.backward(26)
t.forward(13)


t.penup()
t.goto(-40,0)
t.pendown()
#K
t.right(90)
t.forward(40)
t.backward(20)
t.right(45)
t.forward(29)
t.backward(29)
t.right(90)
t.forward(29)


t.penup()
t.goto(-5,0)
t.pendown()
#R
t.left(135)
t.forward(40)
t.right(90)
t.circle(-10,180)
t.left(135)
t.forward(27)

t.penup()
t.goto(25,0)
t.pendown()

#A
t.left(120)
t.forward(45)
t.right(150)
t.forward(45)
t.backward(20)
t.right(105)
t.forward(15)

t.penup()
t.goto(65,0)
t.pendown()

turtle.done()


