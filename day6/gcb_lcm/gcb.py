def gcb(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for n in range(x, 0, -1):
        if x % n == 0 and y % n == 0:
            return n
