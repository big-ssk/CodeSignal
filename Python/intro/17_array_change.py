# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg

def array_change(array):
    result = 0

    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            result += (array[i] + 1) - array[i + 1]
            array[i + 1] = array[i] + 1

    return result
