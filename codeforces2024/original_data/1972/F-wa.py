def dfs(x, visited, stable_state, b):
    if visited[x]:
        return stable_state[x]
    visited[x] = True
    next_value = b[x - 1]
    stable_state[x] = dfs(next_value, visited, stable_state, b)
    return stable_state[x]

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
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + m]))
        index += m

        # Determine stable states
        visited = [False] * (m + 1)
        stable_state = [0] * (m + 1)
        for i in range(1, m + 1):
            if not visited[i]:
                dfs(i, visited, stable_state, b)

        # Transform array a to its stable states
        new_a = [stable_state[x] for x in a]

        # Check if it's possible to make a non-decreasing
        if sorted(new_a) != new_a:
            results.append(-1)
            continue

        # Count transformations needed
        transform_count = {}
        for x in a:
            if x not in transform_count:
                count = 0
                current = x
                while current != stable_state[current]:
                    current = b[current - 1]
                    count += 1
                transform_count[x] = count

        # Minimize the number of tricks
        counts = sorted(transform_count.values())
        tricks = 0
        while counts:
            max_count = counts.pop()
            tricks += 1
            while counts and counts[-1] == max_count:
                counts.pop()

        results.append(tricks)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

# Example usage:
# solve()