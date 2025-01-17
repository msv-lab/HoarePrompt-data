def func_1(fountain, n, m):
    (r, c) = fountain
    diagonal_distance = abs(r + c - (n + 1))
    return max(diagonal_distance // 2, 0)

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        alpha = (n * m + 1) // 2
        additional_areas = []
        for __ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            additional_areas.append(func_1((r, c), n, m))
        results.append((alpha, additional_areas))
    for result in results:
        (alpha, additional_areas) = result
        print(alpha)
        print(' '.join(map(str, additional_areas)))
if __name__ == '__main__':
    func_2()