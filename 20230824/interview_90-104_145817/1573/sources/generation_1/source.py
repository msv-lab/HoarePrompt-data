n, d = map(int, input().split())

friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))

friends.sort()

max_friendship = 0
left = 0
right = 0
total_money = friends[0][0]

while right < n:
    if friends[right][0] - friends[left][0] < d:
        total_money += friends[right][0]
        max_friendship = max(max_friendship, total_money)
        right += 1
    else:
        total_money -= friends[left][0]
        left += 1

print(max_friendship)