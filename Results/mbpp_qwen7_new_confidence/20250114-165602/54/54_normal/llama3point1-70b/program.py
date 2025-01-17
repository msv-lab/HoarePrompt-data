def kth_element(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")
    return arr[k-1]
