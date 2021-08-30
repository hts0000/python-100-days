# 输入一个正整数判断是不是素数

is_prime = False
num = int(input("请输入一个正整数: "))

for i in range(2, num + 1):
    if num % i == 0:
        is_prime = True

print(is_prime)
