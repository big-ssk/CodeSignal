# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

def box_blur_v1(image):
    rows = len(image)
    columns = len(image[0])
    res = []
    for i in range(1, rows - 1):
        row = []
        for j in range(1, columns - 1):
            row.append(sum([image[i + x][j + y] for x in [-1, 0, 1] for y in [-1, 0, 1]]) // 9)
        res.append(row)
    return res


def box_blur_v2(image):
    res = []
    for i in range(len(image) - 2):
        res.append([])
        for j in range(len(image[0]) - 2):
            res[i].append(sum(image[i][j:j + 3] + image[i + 1][j:j + 3] + image[i + 2][j:j + 3]) / 9 // 1)
    return res


def box_blur_v3(image):
    return [[int(sum(sum(x[i:i + 3]) for x in image[j:j + 3]) / 9) for i in range(len(image[j]) - 2)] for j in
            range(len(image) - 2)]
