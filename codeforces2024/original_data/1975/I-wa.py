def solve():
    n = int(input())
    c = list(map(int, input().split()))
    s = input()

    draw_pile_initial = []
    hand_initial = []
    for i in range(n):
        if s[i] == '0':
            draw_pile_initial.append(c[i])
        else:
            hand_initial.append(c[i])

    if not draw_pile_initial:
        print(1)
        return

    if not hand_initial:
        print(0)
        return

    has_positive_power_in_hand = any(power > 0 for power in hand_initial)

    if has_positive_power_in_hand:
        print(1)
    else:
        print(0)

t = int(input())
for _ in range(t):
    solve()