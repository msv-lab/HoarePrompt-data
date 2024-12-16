def find_Index(n):
    import math
    idx = 1
    while True:
        triangular_num = (idx * (idx + 1)) // 2
        if len(str(triangular_num)) >= n:
            return idx
        idx += 1
