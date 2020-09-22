# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5

from itertools import count


def avoid_obstacles(a):
    for i in count(2):
        if all(x % i != 0 for x in a):
            return i
