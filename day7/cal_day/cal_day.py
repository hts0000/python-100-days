import re


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# date = "2020-08-19"
def cal_day(date):
    if re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date) == None:
        return None

    date = date.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ][is_leap_year(year)]
    # True == 1  False == 0

    totle = 0
    for idx in range(month - 1):
        totle += days_of_month[idx]
    return totle + day


def main():
    date = "2020-08-19"
    print(cal_day(date))


if __name__ == "__main__":
    main()
