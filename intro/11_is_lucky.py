# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def is_lucky(n):
    n = [int(x) for x in str(n)]
    mid = int(len(n) / 2)
    return True if sum(n[:mid]) == sum(n[mid:]) else False
