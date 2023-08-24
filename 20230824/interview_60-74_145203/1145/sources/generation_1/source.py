n = int(input())
badges = list(map(int, input().split()))

sorted_badges = sorted(badges)
coins = 0

for i in range(1, n):
    if sorted_badges[i] <= sorted_badges[i-1]:
        coins += sorted_badges[i-1] - sorted_badges[i] + 1
        sorted_badges[i] = sorted_badges[i-1] + 1

print(coins)