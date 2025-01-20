# Read input from standard input
x_p, y_p, x_v, y_v = map(int, input().split())

# Calculate the maximum distances to (0, 0) for both players
polycarp_distance = max(x_p, y_p)
vasiliy_distance = max(x_v, y_v)

# Determine the winner based on the distances
if polycarp_distance <= vasiliy_distance:
    print("Polycarp")
else:
    print("Vasiliy")
