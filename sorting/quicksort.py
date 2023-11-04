def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high, 1):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)
    return i


def quick_sort(arr, low, high):
    if high <= low:
        return
    p = partition(arr, low, high)
    quick_sort(arr, low, p - 1)
    quick_sort(arr, p + 1, high)


def sort(arr):
    if arr is None or len(arr) == 0:
        return

    quick_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == '__main__':
    print(sort([6, 34, 5, 67, 34, 5, 3455, 6346, 54, 76, 867, 48, 564, 745, 67, 567, 4, 56]))
