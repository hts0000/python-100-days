def sum(list1):
    list1.sort()
    return list1[-1], list1[-2]


def main():
    list1 = [1, 2, 3, 4, 5, 6]
    list1 = [8, 2, 1, 6, 7, 5]
    s1, s2 = sum(list1)
    print(s1, s2)


if __name__ == "__main__":
    main()
