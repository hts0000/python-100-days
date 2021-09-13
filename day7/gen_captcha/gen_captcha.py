import random

# 生成器
def gen(code_len=4):
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(code_len):
        yield all_chars[random.randint(0, len(all_chars) - 1)]


def gen_captcha(code_len=4):
    captcha = ""
    for code in gen(code_len):
        captcha += code
    return captcha


def main():
    code_len = 6
    captcha = gen_captcha(code_len)
    print(captcha)


if __name__ == "__main__":
    main()
