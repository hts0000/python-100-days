def is_palindrome(num=0):
    if num == 0:
        return False

    temp, totle = num, 0
    while temp > 0:
        totle = totle * 10 + temp % 10
        temp //= 10
    return totle == num


def is_prime(num=0):
    if num == 0:
        return False

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True if num != 1 else False


def is_prime_palindrome(num=0):
    return is_palindrome(num) and is_prime(num)


if __name__ == "__main__":
    print(is_prime_palindrome(133020331))
