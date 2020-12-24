import turtle as t
import random as r

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()

color_list = [(176, 173, 4), (188, 2, 77), (4, 147, 60), (245, 63, 4), (87, 2, 91), (4, 127, 202), (250, 75, 9),
              (43, 191, 232), (246, 20, 149), (241, 163, 32), (247, 221, 34), (185, 5, 2), (226, 17, 133),
              (252, 225, 0), (253, 4, 7), (253, 8, 4)]

# get tim to initial starting position.
tim.penup()
tim.setposition(-200, -200)


def draw_hirst(y_coordinate):
    """takes current y position of turtle """
    # draw circles
    for _ in range(10):
        tim.dot(20, r.choice(color_list))
        tim.forward(50)
    # move to next line
    tim.sety(y_coordinate + 50)
    tim.setx(-200)


for _ in range(10):
    draw_hirst(tim.ycor())

screen = t.Screen()
screen.screensize(400, 400)
screen.exitonclick()
