def find_first_occurrence(arr, num):
    for i, x in enumerate(arr):
        if x == num:
            return i
    return -1  # return -1 if num is not found in the array
