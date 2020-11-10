def fileNaming(names):

    def rename(name):
        counter = 1
        new = f'{name}({counter})'
        while new in res:
            counter += 1
            new = f'{name}({counter})'
        return new

    res = []

    for name in names:
        if name in res:
            name = rename(name)
        res.append(name)

    return res
