# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def sort_by_height(array):
    sorted_people = (x for x in sorted(array) if x != -1)
    result = []

    for i in array:
        result.append(i if i == -1 else next(sorted_people))

    return result
