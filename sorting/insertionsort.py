def insertion_sort(arr):
    if not arr:
        return []

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
    return arr


if __name__ == "__main__":
    print(insertion_sort(
        [432, 52, 5234, 23, 4, 64, 65, 6, 456, 34, 534, 5, 3241, 6, 34, 5, 67, 34, 5, 3455, 6346, 54, 76, 867, 48, 564,
         745, 67, 567, 4, 56]))
