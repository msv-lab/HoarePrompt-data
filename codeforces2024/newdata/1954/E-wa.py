def min_seconds_to_kill_monsters(n, health):
    max_health = max(health)
    results = []

    for k in range(1, max_health + 1):
        # Copy the health list to simulate the process
        current_health = health[:]
        operations = 0

        for i in range(n):
            if current_health[i] > 0:
                # Apply chain lightning at position i
                operations += 1
                # Damage the current monster
                current_health[i] -= k
                # Damage the left neighbor if it exists
                if i > 0:
                    current_health[i - 1] -= k
                # Damage the right neighbor if it exists
                if i < n - 1:
                    current_health[i + 1] -= k

        results.append(operations)

    return results

# Read input
n = int(input().strip())
health = list(map(int, input().strip().split()))

# Get the results
results = min_seconds_to_kill_monsters(n, health)

# Print the results
for result in results:
    print(result)