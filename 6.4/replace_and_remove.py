def replace_and_remove(arr, size=None):

    return arr.replace('a', 'dd').replace('b', '')[0:size]


assert replace_and_remove('acdbbca') == 'ddcdcdd'
assert replace_and_remove('acdbbca', 4) == 'ddcd'
