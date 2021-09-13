def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""


def get_suffix(file_name=""):
    if file_name == "":
        return ""

    for idx, str in enumerate(file_name):
        if str == ".":
            return file_name[idx + 1 :]
    return file_name


def main():
    file_name = "testtxt"
    suffix = get_suffix(file_name)
    print(suffix)


if __name__ == "__main__":
    main()
