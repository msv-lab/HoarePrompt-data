n = int(input())
ratings = list(map(int, input().split()))
ratings.sort(reverse=True)
can_win = True
for i in range(n):
    if ratings[i] <= ratings[n+i]:
        can_win = False
        break
print("YES" if can_win else "NO")
