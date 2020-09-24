# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def adjacent_elements_product(array):
    maximum = None
    for i in range(1, len(array)):
        current = array[i - 1] * array[i]
        if maximum is None or current > maximum:
            maximum = current
    return maximum
