### Sierpinski Triangle

import turtle

def draw_triangle(points, colors, t):
	t.fillcolor(colors)
	t.up()
	t.goto(points[0][0], points[0][1])
	t.down()
	t.begin_fill()
	t.goto(points[1][0], points[1][1])
	t.goto(points[2][0], points[2][1])
	t.goto(points[0][0], points[0][1])
	t.end_fill()

def get_mid(p1, p2):
	return((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def triangle(points, degree, t):
	colors = ['blue', 'red', 'green', 'white',
	 'yellow', 'violet', 'ornge']
	draw_triangle(points, colors[degree], t)
	if degree > 0:
	 	triangle([points[0],
	 		get_mid(points[0], points[1]),
	 		get_mid(points[0], points[2])],
	 		degree -1, t)
	 	triangle([points[1],
	 		get_mid(points[0], points[1]),
	 		get_mid(points[1], points[2])],
	 		degree -1, t)
	 	triangle([points[2],
	 		get_mid(points[2], points[1]),
	 		get_mid(points[0], points[2])],
	 		degree -1, t)


def main():
	t = turtle.Turtle()
	win = turtle.Screen()
	my_points = [[-100, -50], [0,100], [100, -50]]
	triangle(my_points, 3, t)
	win.exitonclick()

main()