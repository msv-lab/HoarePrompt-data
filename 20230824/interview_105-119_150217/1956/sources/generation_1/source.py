def determine_game_results(t, rounds):
    can_win = 0
    can_lose = 0

    for i in range(t):
        s, e = rounds[i]
        #Check if Lee can always win
        if (e - s) % 2 == 1:
            can_win = 1

        #Check if Lee can always lose
        if e // 2 < s:
            can_lose = 1

    print(can_win, can_lose)


t = int(input())
rounds = []
for _ in range(t):
    s, e = map(int, input().split())
    rounds.append((s, e))

determine_game_results(t, rounds)