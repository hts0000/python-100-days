from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(roll_dice())
print(roll_dice(3))
print(add(1, 2, 3))
print(add())
