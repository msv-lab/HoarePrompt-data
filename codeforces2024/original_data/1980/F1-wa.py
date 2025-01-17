def solve():
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

        fountains = []
        for __ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            fountains.append((r, c))

        # Calculate the maximum area Alice can have without any fountains
        alpha = (n * m + 1) // 2

        # Determine the impact of each fountain
        a = [0] * k
        for i, (r, c) in enumerate(fountains):
            if r == 1 or c == 1 or r == n or c == m:
                a[i] = 1

        results.append((alpha, a))

    for result in results:
        print(result[0])
        print(' '.join(map(str, result[1])))

# Example usage
if __name__ == "__main__":
    solve()