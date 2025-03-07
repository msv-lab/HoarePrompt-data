def func_1():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        wins += 1
    if wins >= k:
        print(wins - 1)
        return
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        win_with_swap += 1
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
if __name__ == '__main__':
    t = int(input())
for _ in range(t):
    func_1()