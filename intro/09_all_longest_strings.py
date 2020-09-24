# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

def all_longest_strings(array):
    max_len = max(len(i) for i in array)
    result = []

    for i in array:
        if len(i) == max_len:
            result.append(i)

    return result
