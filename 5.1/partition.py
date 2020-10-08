def partition_by_pivot(arr, pivot_index):
    i = 0
    end = len(arr)
    while(i < end):
        if (i < pivot_index and arr[i] > arr[pivot_index]):
            arr.append(arr.pop(i))
            pivot_index -= 1
            end -= 1
        else:
            if (i > pivot_index and arr[i] < arr[pivot_index]):
                arr.insert(0, arr.pop(i))
                pivot_index += 1
            elif (i != pivot_index and arr[i] == arr[pivot_index]):
                arr.insert(pivot_index + 1, arr.pop(i))
            i += 1

    return arr


print(partition_by_pivot([0, 1, 2, 0, 2, 1, 1], 0))
print(partition_by_pivot([0, 1, 2, 0, 2, 1, 1], 1))
print(partition_by_pivot([0, 1, 2, 0, 2, 1, 1], 2))
