def my_pow(x, y):
    if y == 0:
        return 1

    result = x
    for i in range(1, y):
        result *= x

    return result


def pow_rec(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == 2:
        return x * x
    else:
        return x * pow_rec(x, y - 1)


assert(my_pow(7, 0) == 1)
assert(my_pow(0, 0) == 1)
assert(my_pow(2, 4) == 16)
assert(my_pow(8, 8) == 16777216)
assert(my_pow(100, 4) == 100000000)

assert(pow_rec(7, 0) == 1)
assert(pow_rec(0, 0) == 1)
assert(pow_rec(2, 4) == 16)
assert(pow_rec(8, 8) == 16777216)
assert(pow_rec(100, 4) == 100000000)
