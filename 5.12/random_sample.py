import random

def random_sample(arr, size):

    while(len(arr) > size):
        arr.pop(random.randint(0, len(arr) - 1))

    return arr


assert random_sample([1, 2, 3, 4], 0) == []
assert random_sample([1, 2, 3, 4], 4) == [1, 2, 3, 4]
assert random_sample([1, 2, 3, 4], 9) == [1, 2, 3, 4]
assert len(random_sample([1, 2, 3, 4], 2)) == 2
