(n, pos, l, r) = map(int, input().split())
if l == 1 and r == n:
    print(0)
elif l == 1:
    print(abs(pos - r) + 1)
elif r == n:
    print(abs(pos - l) + 1)
else:
    move_to_l = abs(pos - l)
    move_to_r = abs(pos - r)
    close_both_sides = min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))
    print(close_both_sides)