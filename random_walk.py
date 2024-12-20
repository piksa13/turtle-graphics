import random
import turtle
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("circle")
jimmy.pensize(15)
jimmy.speed(15.0)
angles = [0, 90, 180, 270]
turtle.colormode(255)

def color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk(no_of_steps = 100):
    for _ in range(no_of_steps):
        jimmy.color(color_generator())
        jimmy.forward(30)
        jimmy.setheading(random.choice(angles))


random_walk(50)
screen = Screen()
screen.exitonclick()