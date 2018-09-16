import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	imzoughene = turtle.Turtle()
	imzoughene.shape("turtle")
	imzoughene.color("yellow")
	imzoughene.speed(2)
	i=0
	while(i<4):
		imzoughene.forward(100)
		imzoughene.right(90)
		i=i+1
	youssef = turtle.Turtle()
	youssef.shape("arrow")
	youssef.color("blue")
	youssef.speed(2)
	youssef.circle(70)
	window.exitonclick()
draw_square()