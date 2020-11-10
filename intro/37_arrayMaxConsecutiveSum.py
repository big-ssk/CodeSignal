def arrayMaxConsecutiveSum(inputArray, k):
    res = window = sum(inputArray[:k])
    n = len(inputArray)
    for i in range(n - k):
        window = window - inputArray[i] + inputArray[i + k]
        res = max(window, res)
    return res
    
