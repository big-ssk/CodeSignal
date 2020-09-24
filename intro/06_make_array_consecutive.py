# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def make_array_consecutive2(statues):
    items = max(statues) - min(statues)
    return items - len(statues) + 1
