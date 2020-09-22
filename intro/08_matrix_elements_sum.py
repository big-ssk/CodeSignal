# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr/solutions

def matrix_elements_sum(matrix):

    result = 0
    banned_idx = []

    for row in matrix:
        for el_idx in range(len(row)):
            if row[el_idx] <= 0:
                banned_idx.append(el_idx)
            if el_idx in banned_idx:
                continue
            else:
                result += row[el_idx]

    return result
