t = int(input())
rounds = []
for _ in range(t):
    s, e = map(int, input().split())
    rounds.append((s, e))
    
can_win = 1
can_lose = 1

for i in range(t):
    s, e = rounds[i]

    # Check if Lee can always win
    if (e - s) % 2 != 0:
        can_win = 0

    # Lee can always lose if the condition is not met
    can_lose = 1

print(can_win, can_lose)