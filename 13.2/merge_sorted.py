def merge(a, b):
    a_idx = a.index(None) - 1  # Last non-None element
    b_idx = len(b) - 1  # Assume b has no trailing Nones
    write_idx = a_idx + b_idx + 1

    while write_idx >= 0:
        if b_idx >= 0 and a[a_idx] <= b[b_idx]:
            a[write_idx] = b[b_idx]
            b_idx -= 1
        else:
            a[write_idx] = a[a_idx]
            a_idx -= 1
        write_idx -= 1

    return a


assert merge([3, 13, 17, None, None, None, None, None], [3, 7, 11, 19]) == [3, 3, 7, 11, 13, 17, 19, None]
