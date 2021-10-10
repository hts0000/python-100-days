from turtle import *

bar_len = 500
bar_circle_radius = 25


def init_bar(color="black"):
    speed(0)
    hideturtle()
    pencolor(color)
    penup()
    # 居中
    goto(-(bar_len / 2), -(bar_circle_radius / 2))
    pendown()


def draw_bar():
    circle(bar_circle_radius, -180)
    bk(bar_len)
    circle(bar_circle_radius, -180)
    bk(bar_len)
    circle(bar_circle_radius, -90)
    left(90)
    penup()
    fd(bar_circle_radius)
    pendown()


init_bar()
draw_bar()

speed(1)
pensize(bar_circle_radius * 2 - bar_circle_radius / 5)
pencolor("red")
fd(bar_len)

done()
