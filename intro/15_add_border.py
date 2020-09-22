# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

def add_border_v1(picture):
    result = [''.center(len(picture[0]) + 2, '*')]

    for i in picture:
        result.append(i.center(len(i) + 2, '*'))
    result.append(''.center(len(picture[0]) + 2, '*'))

    return result


def add_border_v2(picture):
    n = len(picture[0]) + 2
    return ["*" * n] + [x.center(n, "*") for x in picture] + ["*" * n]
