import functools
import time


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
    for args, expected in [
        ((7, 0), 1),
        ((0, 0), 1),
        ((2, 2), 4),
        ((2, 3), 8),
        ((2, 4), 16),
        ((8, 8), 16777216),
        ((100, 4), 100000000),
        ((2, 50), 1125899906842624),
        ]:

        tic = time.perf_counter()
        actual = f(*args)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Case: {args}, Elapsed time: {elapsed_time:0.9f} seconds")

        assert actual == expected
