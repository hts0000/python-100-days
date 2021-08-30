import math

circle_radius = 0.0
circumference = 0.0
circle_area = 0.0

circle_radius = float(input("circle radius = "))
circumference = circle_radius * 2 * math.pi
circle_area = circle_radius * circle_radius * math.pi

print(
    f"radius {circle_radius: .2f}, circumference {circumference: .2f}, \
circle_area {circle_area: .2f}"
)

print(
    "radius = %.2f, circumference = %.2f, circle_area = %.2f"
    % (circle_radius, circumference, circle_area)
)
