def longestDigitsPrefix(inputString):
    res = ''
    i = 0
    while i < len(inputString):
        if inputString[i].isdigit():
            res += str(inputString[i])
        else:
            return res
        i += 1
    return res
