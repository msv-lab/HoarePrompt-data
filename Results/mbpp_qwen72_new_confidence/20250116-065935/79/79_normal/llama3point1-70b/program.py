def zero_count(arr):
    zeros = arr.count(0)
    non_zeros = len(arr) - zeros
    if non_zeros == 0:
        return 0
    return zeros / non_zeros
