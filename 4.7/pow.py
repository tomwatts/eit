def pow(x, y):
    if y == 0:
        return 1

    result = x
    for i in range(1, y):
        result *= x

    return result

assert(pow(7, 0) == 1)
assert(pow(0, 0) == 1)
assert(pow(2, 4) == 16)
assert(pow(8, 8) == 16777216)
assert(pow(100, 4) == 100000000)
