import math


def solve():
    k, x, c = map(int, input().split())
    coins_lost = 0
    check = True
    for i in range(x):
        bet_needed = coins_lost // (k-1) + 1
        coins_lost += bet_needed
        if coins_lost > c:
            check = False
            break

    win = (c - coins_lost) * k
    if win > c and check:

        print('YES')
    else:
        print('NO')






for i in range(int(input())):
    solve()