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

	benfarice= turtle.Turtle()
	benfarice.shape("turtle")
	benfarice.color("green")
	benfarice.speed(2)
	benfarice.forward(100)

	i=0
	while (i<2):
		benfarice.left(120)
		benfarice.forward(100)
		i=i+1
	window.exitonclick()
draw_square()