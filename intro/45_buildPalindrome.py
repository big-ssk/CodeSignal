def buildPalindrome(st):
    if st == st[::-1]:
        return st

    def is_palindrome(st):
        return st == st[::-1]

    n = len(st)

    for i in range(n):
        subst = st[i:n]
        if is_palindrome(subst):
            part = st[:i]
            return st + part[::-1]
