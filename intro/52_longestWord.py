def longestWord(text):
    n = 0
    s = ''
    for i in re.findall(r'[a-zA-Z]+', text):
        if len(i) > n:
            n = len(i)
            s = i
    return s

