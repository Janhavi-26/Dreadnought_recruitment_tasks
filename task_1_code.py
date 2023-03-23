## displaying logo of youtube music using turtle.
import turtle
turtle_1=turtle.Turtle()
turtle_1.shape("arrow")
turtle_1.color("red")

## making red circle
turtle_1.fillcolor("red")
turtle_1.begin_fill()
turtle_1.circle(100)
turtle_1.end_fill()

## making a white circle outline
turtle_1.penup()
turtle_1.goto(0,40)
turtle_1.pendown()
turtle_1.color("white")
turtle_1.width(5)
turtle_1.circle(60)

## making a triangle in the middle
turtle_1.penup()
turtle_1.goto(-20,70)
turtle_1.pendown()
turtle_1.fillcolor("white")
turtle_1.begin_fill()
turtle_1.left(90)
turtle_1.forward(60)
turtle_1.right(120)
turtle_1.forward(60)
turtle_1.right(120)
turtle_1.forward(60)
turtle_1.end_fill()
turtle_1.hideturtle()
