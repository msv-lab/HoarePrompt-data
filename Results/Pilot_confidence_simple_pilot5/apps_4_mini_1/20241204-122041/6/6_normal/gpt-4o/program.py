# Read input
n, pos, l, r = map(int, input().split())

# Check the initial conditions
if l == 1 and r == n:
    # No tabs need to be closed
    print(0)
elif l == 1:
    # Only need to close the tabs to the right
    print(abs(pos - r) + 1)
elif r == n:
    # Only need to close the tabs to the left
    print(abs(pos - l) + 1)
else:
    # Need to close tabs on both sides
    move_to_l = abs(pos - l)
    move_to_r = abs(pos - r)
    close_both_sides = min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))
    print(close_both_sides)

