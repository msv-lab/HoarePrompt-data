def count_valid_terms(b1, q, l, m, bad_numbers):
    bad_set = set(bad_numbers)
    count = 0

    if abs(b1) > l:
        return 0

    if b1 == 0:
        if 0 in bad_set:
            return 0
        else:
            return float('inf')

    if q == 0:
        if b1 in bad_set:
            return 0
        if 0 in bad_set:
            return 1
        return float('inf')

    if q == 1:
        if b1 in bad_set:
            return 0
        return float('inf')

    if q == -1:
        if b1 in bad_set and -b1 in bad_set:
            return 0
        return float('inf')

    current = b1
    while abs(current) <= l:
        if current not in bad_set:
            count += 1
        current *= q

        if q == 1 or q == -1 or q == 0:
            break

    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    b1 = int(data[0])
    q = int(data[1])
    l = int(data[2])
    m = int(data[3])
    bad_numbers = list(map(int, data[4:4 + m]))

    result = count_valid_terms(b1, q, l, m, bad_numbers)
    if result == float('inf'):
        print("inf")
    else:
        print(result)
