def find_Index(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        if len(str(triangular_number)) == n:
            return k
        k += 1

# Test cases
assert find_Index(2) == 4
assert find_Index(3) == 14
assert find_Index(4) == 45
