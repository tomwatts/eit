def spiral(arr):
    result = list()

    if len(arr) == 1:
        return [arr[0][0]]
    else:  # Loop around outside and then append sub array, if needed
        result += arr[0]

        for i in range(1, len(arr)):
            result.append(arr[i][-1])

        result += arr[-1][-2::-1]

        for i in range(len(arr) - 2, 0, -1):
            result.append(arr[i][0])

        sub_array = [row[1:-1] for row in arr[1:-1]]
        if len(sub_array) > 0:
            result += spiral(sub_array)

    return result

assert spiral([[1]]) == [1]
assert spiral([[1, 2], [3, 4]]) == [1, 2, 4, 3]
assert spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
