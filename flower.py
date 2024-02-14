import turtle

tr=turtle.Turtle()

tr.pensize(3)
tr.speed(10)

tr.fillcolor("Yellow")
tr.color("Yellow")
tr.penup
tr.goto(-55,-69)
tr.begin_fill()
tr.pendown
tr.circle(50)
tr.end_fill()

tr.color("Red")
tr.pendown()
tr.fillcolor("Red")
for i in range(6):
    tr.penup()
    tr.goto(-55+i, -20) 
    tr.begin_fill() 
    tr.setheading(60*i)  
    tr.forward(54)
    tr.left(75)
    tr.pendown()
    tr.circle(-60)
    tr.end_fill()


tr.penup()
tr.goto(-55,-79)
tr.setheading(90)
tr.pendown()
tr.pensize(6)
tr.speed(2)
tr.color("Green")
tr.sety(-400)


