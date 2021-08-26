side1 = float(input("三角形边长1: "))
side2 = float(input("三角形边长2: "))
side3 = float(input("三角形边长3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("周长为: %f\n" % (side1 + side2 + side3))
    p = (side1 + side2 + side3) / 2
    area = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
    print("面积为: %f\n" % area)
else:
    print("无法组成三角形")
