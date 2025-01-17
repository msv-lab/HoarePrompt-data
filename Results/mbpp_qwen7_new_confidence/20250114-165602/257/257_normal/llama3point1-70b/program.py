def find_kth(arr1, arr2, k):
    merged = sorted(arr1 + arr2)
    return merged[k-1]
