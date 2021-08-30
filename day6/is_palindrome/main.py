def is_palindrome(num=0):
    if num == 0:
        return False
    temp = num
    totle = 0
    while temp > 0:
        totle = totle * 10 + temp % 10
        temp //= 10
    return totle == num


if __name__ == "__main__":
    print(is_palindrome(0))
