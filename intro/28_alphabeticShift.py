def alphabeticShift(a):
    from string import ascii_lowercase as letters

    table = ''.maketrans(letters, letters[1:] + letters[:1])
    return a.translate(table)
