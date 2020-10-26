def merge(a, b):
    j = 0
    for i in b:
        while j < len(a) and a[j] < i:
            j += 1

        if j >= len(a):
            a.append(i)
        else:
            # Could avoid insert by building separate result array
            a.insert(j, i)

    return a


assert merge([3, 13, 17], [3, 7, 11, 19]) == [3, 3, 7, 11, 13, 17, 19]
