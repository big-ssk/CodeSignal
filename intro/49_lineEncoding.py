def lineEncoding(s):
    current = s[0]
    counter = 0
    i = 0
    res = ''
    while i < len(s):
        if s[i] == current:
            counter += 1
        else:
            res += f'{counter if counter > 1 else ""}{s[i - 1]}'
            current = s[i]
            counter = 1
        i += 1
    res += f'{counter if counter > 1 else ""}{s[i - 1]}'
    return res
