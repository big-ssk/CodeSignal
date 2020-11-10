def digitsProduct(product):
    if not product:
        return 10

    if product < 10:
        return product

    res = []

    for i in range(9, 1, -1):
        while product % i == 0:
            res.append(str(i))
            product /= i

    if product > 1:
        return -1

    return int(''.join(sorted(res)))
