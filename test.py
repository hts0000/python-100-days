from random import random
import turtle as t
from math import sqrt

darts = 10000
hits = 0
t.penup()
t.speed(0)
t.tracer(False)
for _ in range(darts):
    x = random()
    y = random()
    dist = sqrt(x ** 2 + y ** 2)
    t.goto(x * 300, y * 300)
    t.pendown()
    if dist <= 1.0:
        hits += 1
        t.dot(2, "red")
    else:
        t.dot(2, "blue")
    t.penup()
t.tracer(True)
print(4 * (hits / darts))
t.goto(110, -30)
pi = "pi=" + str(4 * (hits / darts))
t.write(pi, font=("consolas", 15, "normal"))
t.exitonclick()
