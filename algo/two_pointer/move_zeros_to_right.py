def zero_to_right(arr, debug=False):
    """
    moves all zeros within the array to its right, without changing the order of non-zero element.
    TC O(n)
    SC O(1)
    """
    left = 0

    for right in range(len(arr)):
        if arr[right] != 0:
            tmp = arr[right]
            arr[right] = arr[left]
            arr[left] = tmp
            left += 1

        if debug:
            print("============")
            print(arr)
            print("left:", left)
            print("right: ", right)

    return arr


if __name__ == "__main__":
    print(zero_to_right([0, 0, 0, 1, 2, 3, 5, 0, 23, 4, 234, 0]))
    print(zero_to_right([0, 0, 0, 1, 2, 3, 5, 0, 23, 4, 234, 2323]))
    print(zero_to_right([23, 0, 0, 1, 2, 3, 5, 0, 23, 4, 234, 2323], True))
