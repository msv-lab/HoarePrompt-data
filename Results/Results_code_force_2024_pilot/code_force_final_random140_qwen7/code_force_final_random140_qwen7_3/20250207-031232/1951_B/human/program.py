def win():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        wins += 1
 
    if wins >= k:
        print(wins - 1)
        
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        wins_with_swap += 1
 
    print(max(wins- 1, wins_with_swap - wins - 1 + (wins> 0)))
 
t = int(input())
for _ in range(t):
    win()