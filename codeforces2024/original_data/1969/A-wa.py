def min_invitations(t, test_cases):
    results = []
    for case in test_cases:
        n, p = case
        visited = [False] * n
        cycles = []

        # Find all cycles in the permutation
        for i in range(n):
            if not visited[i]:
                cycle_length = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = p[x] - 1  # move to the best friend
                    cycle_length += 1
                cycles.append(cycle_length)

        # Calculate the minimum number of invitations
        if len(cycles) == 1:
            # If there's only one cycle, we need to invite all but one in the cycle
            min_invitations = cycles[0]
        else:
            # If there are multiple cycles, we need to ensure at least two friends attend
            # We can invite all but one in the largest cycle, and one from another cycle
            min_invitations = sum(cycles) - max(cycles) + 1

        results.append(min_invitations)

    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    p = list(map(int, data[index+1:index+1+n]))
    test_cases.append((n, p))
    index += n + 1

# Get results
results = min_invitations(t, test_cases)

# Print results
for result in results:
    print(result)