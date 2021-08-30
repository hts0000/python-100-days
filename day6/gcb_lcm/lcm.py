import gcb


def lcm(x, y):
    return x * y // gcb.gcb(x, y)
