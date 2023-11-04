def selection_sort(arr):
    if not arr:
        return []

    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr


if __name__ == "__main__":
    print(selection_sort([]))

    print(selection_sort(None))

    print(selection_sort(
        [432, 52, 5234, 23, 4, 64, 65, 6, 456, 34, 534, 5, 3241, 6, 34, 5, 67, 34, 5, 3455, 6346, 54, 76, 867, 48, 564,
         745, 67, 567, 4, 56]))
