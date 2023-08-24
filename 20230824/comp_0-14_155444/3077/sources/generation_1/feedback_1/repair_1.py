def calculate_max_minions_destroyed(n, m, r, villages, minions):
    max_destroyed = float('-inf')

    # Iterate over all possible attack centers
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            center = [i, j]  # Possible attack center

            # Calculate the distance between the attack center and all villages
            distances_from_center = [((v[0] - center[0]) ** 2 + (v[1] - center[1]) ** 2) ** 0.5 for v in villages]

            # Count the number of villages that are outside the attack radius
            villages_outside_radius = sum([distance > v[2] + r for distance, v in zip(distances_from_center, villages)])

            # Calculate the number of minions that can be destroyed
            minions_destroyed = m - villages_outside_radius

            # Update the maximum number of minions destroyed
            max_destroyed = max(max_destroyed, minions_destroyed)

    return max_destroyed

# Read input
n, m, r = map(int, input().split())
villages = []
minions = []
for _ in range(n):
    vx, vy, vr = map(int, input().split())
    villages.append((vx, vy, vr))
for _ in range(m):
    mx, my = map(int, input().split())
    minions.append((mx, my))

# Calculate the maximum number of minions destroyed
result = calculate_max_minions_destroyed(n, m, r, villages, minions)

# Print the result
print(result)