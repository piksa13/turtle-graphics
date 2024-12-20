import turtle
import colorgram
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("arrow")
jimmy.pensize(2)
jimmy.speed(30.0)
turtle.colormode(255)
jimmy.teleport(x= -250, y= -250, fill_gap=False)

def extracting_colors_from_image(number_of_colors = 100):
    colors = colorgram.extract('image.jpg', number_of_colors)
    color_list_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors ]
    return color_list_rgb

extracted_colours = extracting_colors_from_image()

def hirst_painting(dot_size = 20, no_rows = 10, no_columns = 10, list_of_colours = extracted_colours, gap = 50):
    i = 0
    for column in range(no_columns):
        init_x_position = jimmy.position()[0]
        for row in range(no_rows):
            jimmy.dot(dot_size, list_of_colours[i])
            i = i + 1
            if i >= len(list_of_colours):
                i = 0
            x_distance = jimmy.position()[0] + gap
            jimmy.teleport(x=x_distance, y=None, fill_gap=False)
        y_position = jimmy.position()[1] + gap
        jimmy.teleport(x=init_x_position, y=y_position, fill_gap=False)
    jimmy.hideturtle()

hirst_painting()

screen = Screen()
screen.exitonclick()