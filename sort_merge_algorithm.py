def merge(arr, p, q, r):
    left = arr[p:q]
    right = arr[q:r]
    k = p
    i = 0
    j = 0

    while p + i < q and q + j < r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if p + i < q:
        while k < r:
            arr[k] = left[i]
            i += 1
            k += 1
    else:
        while k < r:
            arr[k] = right[j]
            j += 1
            k += 1


def sort_merge(arr, p, r):
    if p < r - 1:
        q = (p + r) // 2
        sort_merge(arr, p, q)
        sort_merge(arr, q+1, r)
        merge(arr, p, q, r)
        return arr


# A = [5, 2, 4, 6, 1, 3, 2, 6]
# print(sort_merge(A, 0, len(A)))
