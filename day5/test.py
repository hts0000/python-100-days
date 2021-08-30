from random import randint

# from math import sqrt

# 水仙花数
for num in range(100, 1000, 1):
    if (num % 10) ** 3 + (num % 100 // 10) ** 3 + (num // 100) ** 3 == num:
        print(num)

# 正数反转
num = 12345
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(reversed_num)

# 百钱百鸡
for x in range(100):
    for y in range(100):
        if 5 * x + 3 * y + (100 - x - y) / 3 == 100:
            print("公鸡%d, 母鸡%d, 小鸡%d\n" % (x, y, (100 - x - y)))

# CRAPS赌博游戏
money = 000
print("赌局开始")
first = True
while money >= 100:
    debt = int(input("请下注: "))
    while True:
        player_count = randint(1, 6) + randint(1, 6)
        if first:
            print("第一次掷骰子, 点数为%d" % (player_count))
            first_count = player_count
            first = False
            if player_count == 7 or player_count == 11:
                money += debt
                print("玩家胜利, 获得%d¥, 当前余额为%d" % (debt, money))
                first = True
                break
            elif player_count == 2 or player_count == 3 or player_count == 12:
                money -= debt
                print("玩家失败, 失去%d¥, 当前余额为%d" % (debt, money))
                first = True
                break
        else:
            print("本次掷骰子, 点数为%d" % (player_count))
            if player_count == 7:
                money -= debt
                print("玩家失败, 失去%d¥, 当前余额为%d" % (debt, money))
                first = True
                break
            elif player_count == first_count:
                money += debt
                print("玩家胜利, 获得%d¥, 当前余额为%d" % (debt, money))
                first = True
                break
    is_continue = input("继续吗? [y/n]: ")
    if is_continue == "y" or is_continue == "Y":
        is_continue = True
    else:
        is_continue = False
    print()
    if is_continue:
        continue
    else:
        break
print("赌局结束")

# 生成斐波那契数列的前20个数
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=" ")
print()

# 找出10000以内的完美数
for num in range(1, 10001):
    count = 0
    for n in range(1, num):
        if num % n == 0:
            count += n
    if count == num:
        print("%d是完美数" % (num))
