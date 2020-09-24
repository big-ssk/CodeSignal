# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE/solutions?solutionId=dEyg7JQpWdrPTyPbW

def array_maximal_adjacent_difference_v1(a):
    res = 0
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) > res:
            res = abs(a[i] - a[i + 1])
    return res


def array_maximal_adjacent_difference_v2(a):
    return max([abs(a[i] - a[i + 1]) for i in range(len(a) - 1)])
