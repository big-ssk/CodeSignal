# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def are_similar_v1(a, b):
    if len(a) != len(b) or set(a) ^ set(b) or sorted(a) != sorted(b):
        return False

    diff = sum(i != j for i, j in zip(a, b))

    if diff == 0 or diff == 2:
        return True
    return False


def are_similar_v2(a, b):
    return sorted(a) == sorted(b) and sum([i != j for i, j in zip(a, b)]) <= 2
