# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def palindrome_rearranging_v1(string):
    tmp = {x: string.count(x) for x in string if string.count(x) % 2 == 1}
    n = len(string)
    odds = len(tmp)

    if (odds == 1 and n % 2 != 0) or (not odds and n % 2 == 0):
        return True
    return False


def palindrome_rearranging_v2(string):
    return sum([string.count(x) % 2 for x in set(string)]) <= 1
