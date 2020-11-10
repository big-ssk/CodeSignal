from itertools import count
def depositProfit(deposit, rate, threshold):
    for i in count(1):
        deposit += deposit * rate / 100
        if deposit >= threshold:
            return i
    

