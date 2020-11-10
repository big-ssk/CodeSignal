def sumUpNumbers(inputString):
    return sum([int(x) for x in re.findall(r'\d+', inputString)])
