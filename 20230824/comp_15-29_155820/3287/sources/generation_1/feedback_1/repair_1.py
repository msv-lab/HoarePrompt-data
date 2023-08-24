k = int(input())
x = list(map(int, input().split()))

total_loot = 0

for i in range(k - 1, -1, -1):
    max_coins = x[i]
    total_loot += (2**i * (max_coins // 2))
    x[i] -= (x[i] // 2)

print(total_loot % (10**9 + 7))