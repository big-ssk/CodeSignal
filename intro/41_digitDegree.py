def digitDegree(n):   
    i = 0
    while n > 9:
        n = sum(map(int, list(str(n))))
        i += 1
    return i
    
