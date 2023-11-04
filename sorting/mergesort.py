def merge(arr, aux, low, mid, high):
    for k in range(low, high + 1):
        aux[k] = arr[k]

    i = low
    j = mid + 1

    for k in range(low, high + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > high:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1


def merge_sort(arr, aux, low, high):
    if high <= low:
        return

    mid = low + (high - low) // 2
    merge_sort(arr, aux, low, mid)
    merge_sort(arr, aux, mid + 1, high)
    merge(arr, aux, low, mid, high)


def sort(arr):
    if not arr:
        return []

    merge_sort(arr, [0] * len(arr), 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    print(sort(
        [432, 52, 5234, 23, 4, 64, 65, 6, 456, 34, 534, 5, 3241, 6, 34, 5, 67, 34, 5, 3455, 6346, 54, 76, 867, 48, 564,
         745, 67, 567, 4, 56]))
