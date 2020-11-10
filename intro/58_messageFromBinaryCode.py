def messageFromBinaryCode(code):
    return ''.join(map(chr, [int(code[x: x+8], 2) for x in range(0, len(code), 8)]))
