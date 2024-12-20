from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("circle")
jimmy.color("coral")

for step in range(15):
    jimmy.forward(10)
    x_position = (jimmy.position())[0] + 10
    jimmy.teleport(x=x_position, y=None, fill_gap=False)
    # Alternative solution is penup()/ pendown()



screen = Screen()
screen.exitonclick()