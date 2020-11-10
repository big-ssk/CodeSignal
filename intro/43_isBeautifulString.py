from string import ascii_lowercase as letters

def isBeautifulString(s):

    f = [(x, s.count(x)) for x in letters]
    f.sort()
    print(f)

    for x in range(len(f) - 1):
        if f[x + 1][1] > f[x][1]:
            return False

    return True
