from bisect import bisect_left


def intersection(a, b):
    result = []
    b = list(set(b))  # Remove duplicates

    for l in set(a):
        r = bisect_left(b, l)
        # 👇 🏻taken from https://docs.python.org/3.7/library/bisect.html#searching-sorted-lists
        if r < len(b) and b[r] == l:
            result.append(l)

    return result


assert intersection([], []) == []
assert intersection([1, 2, 3], []) == []
assert intersection([], [1, 2, 3]) == []
assert intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert intersection([1, 2], [1, 2, 3]) == [1, 2]
assert intersection([1, 2, 3], [1, 2]) == [1, 2]
assert intersection([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]) == [5, 6, 8]
