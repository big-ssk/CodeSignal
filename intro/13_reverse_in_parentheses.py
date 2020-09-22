# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

def reverse_in_parentheses(string):
    while '(' in string:
        left = string.rfind('(')
        right = string.find(')', left)
        string = string[:left] + string[left + 1:right][::-1] + string[right + 1:]
    return string
