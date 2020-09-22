# https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL

def are_equally_strong_v1(yl, yr, fl, fr):
    return sum((yl, yr)) == sum((fl, fr)) and max(yl, yr) == max(fl, fr)


def are_equally_strong_v2(yl, yr, fl, fr):
    return {yl, yr} == {fl, fr}
