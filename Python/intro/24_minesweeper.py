# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM

import numpy as np


def minesweeper_v1(matrix):
    res = []

    for row in range(len(matrix)):
        res.append([])
        for column in range(len(matrix[0])):
            val = -matrix[row][column]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= row + x < len(matrix) and 0 <= column + y < len(matrix[0]):
                        val += matrix[row + x][column + y]

            res[row].append(val)
    return res


def minesweeper_v2(matrix):
    matrix = np.array(matrix, dtype=int)
    res = np.zeros((matrix.shape[0] + 2, matrix.shape[1] + 2))
    res[1:-1, 1:-1] = matrix
    res = res[:-2, :] + res[1:-1, :] + res[2:, :]
    res = res[:, :-2] + res[:, 1:-1] + res[:, 2:] - matrix
    return res.tolist()
