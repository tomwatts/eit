def brute_pow(x, y):
    if y == 0:
        return 1

    result = x
    for i in range(1, y):
        result *= x

    return result


def rec_pow(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * rec_pow(x, y - 1)


def tree_pow(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        # Split exponent in half, compute halves, then multiply
        half = tree_pow(x, y // 2)
        return half * half * (x if y % 2 else 1)


for f in [brute_pow, rec_pow, tree_pow]:
    assert(f(7, 0) == 1)
    assert(f(0, 0) == 1)
    assert(f(2, 2) == 4)
    assert(f(2, 3) == 8)
    assert(f(2, 4) == 16)
    assert(f(8, 8) == 16777216)
    assert(f(100, 4) == 100000000)
    assert(f(2, 50) == 1125899906842624)
