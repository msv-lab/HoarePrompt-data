def sequential_search(arr, elem):
    for i, x in enumerate(arr):
        if x == elem:
            return (True, i)
    return (False, -1)
