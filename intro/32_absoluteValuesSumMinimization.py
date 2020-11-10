def absoluteValuesSumMinimization(a):
    res = [sum([abs(x - y) for x in a]) for y in a]
    return a[res.index(min(res))]
