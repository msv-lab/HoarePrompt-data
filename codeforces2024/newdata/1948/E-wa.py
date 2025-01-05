t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    q = (2 * (n - 1) + k - 1) // k  # Equivalent to ceil(2(n-1)/k)
    m = (n + q - 1) // q  # Ceiling division to get group size
    a = []
    c = []
    ai_values = list(range(1, n + 1))
    index = 0
    for clique_num in range(1, q + 1):
        clique_size = min(m, n - index)
        for _ in range(clique_size):
            a.append(ai_values[index])
            c.append(clique_num)
            index += 1
    # Output the assignments
    print(' '.join(map(str, a)))
    print(q)
    print(' '.join(map(str, c)))