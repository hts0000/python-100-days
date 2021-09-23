from turtle import *

color = ["red", "yellow", "blue", "green", "pink", "purple"]

setup(800, 600)
pensize(30)

penup()
goto(-330, -250)

pendown()

for i in range(6):
    pencolor(color[i])
    circle(40, 80)
    circle(-40, 80)

circle(40, 80 / 2)
fd(50)

done()
