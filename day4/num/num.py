# 输入两个正整数，计算它们的最大公约数和最小公倍数

x = int(input("请输入正整数x: "))
y = int(input("请输入正整数y: "))

if x < y:
    x, y = y, x

for num in range(x, 0, -1):
    if x % num == 0 and y % num == 0:
        print("%d和%d的最大公约数是%d" % (x, y, num))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // num))
        break
