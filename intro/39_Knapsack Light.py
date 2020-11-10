def knapsackLight(value1, weight1, value2, weight2, maxW):
    m = [0, weight1, weight2]
    p = [0, value1, value2]
    n = len(m) - 1
    f = [[0] * (maxW + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(maxW + 1):
            if j >= m[i]:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - m[i]] + p[i])
            else:
                f[i][j] = f[i - 1][j]
    return f[n][maxW]
