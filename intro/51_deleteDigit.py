def deleteDigit(n):
    n = str(n)
    res = []
    for i in range(len(n)):
        res.append(int(n[:i] + n[i+1:]))
    return max(res)
