def get_first(arr, key):
    l = 0
    u = len(arr) - 1
    occurrences = []

    while (l <= u):
        m = (u + l) // 2

        if arr[m] < key:
            l = m + 1
        else:
            if arr[m] == key:
                occurrences.append(m)
            u = m - 1

    return min(occurrences) if occurrences else -1


assert get_first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108) == 3
assert get_first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285) == 6
assert get_first([1, 1, 1, 1], 1) == 0
assert get_first([], 1) == -1
assert get_first([2, 3, 4, 5, 6, 7, 10], 1) == -1
assert get_first([2, 3, 4, 5, 6, 7, 10], 10) == 6
