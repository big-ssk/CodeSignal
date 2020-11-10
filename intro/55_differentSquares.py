def differentSquares(matrix):
    n = len(matrix)
    m = len(matrix[0])
    k = 2
    res = set()
    for i in range(n - 1):
        for j in range(m - 1):
            res.add(''.join(map(str, matrix[i][j:j+k] + matrix[i+1][j:j+k])))
    return len(res)
