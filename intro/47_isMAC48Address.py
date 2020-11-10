def isMAC48Address(inputString):
    if len(inputString) != 17:
        return False
    try:
        for i in inputString.split('-'):
            if not 0 <= int(i, 16) <= 255:
                return False
    except:
        return False
    return True
