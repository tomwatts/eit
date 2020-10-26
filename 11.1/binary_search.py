def get_first(arr, key):
    l = 0
    u = len(arr) - 1

    while (l <= u):
        m = (u + l) // 2

        if arr[m] == key:
            left_m = get_first(arr[0:m], key)
            if left_m >= 0:  # Found another in the left side
                return left_m
            else:
                return m
        elif arr[m] < key:
            l = m + 1
        else:
            u = m - 1

    return -1


assert get_first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108) == 3
assert get_first([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285) == 6
assert get_first([1, 1, 1, 1], 1) == 0
assert get_first([], 1) == -1
assert get_first([2, 3, 4, 5, 6, 7, 10], 1) == -1
assert get_first([2, 3, 4, 5, 6, 7, 10], 10) == 6
