def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cur_mex = 0
    cur_have = [0] * (n + 1)
    for el in a:
        cur_have[el] += 1
    while cur_have[cur_mex]:
        cur_mex += 1

    another_mex = 0
    another_have = [0] * (n + 1)
    for i in range(n):
        cur_have[a[i]] -= 1
        if cur_have[a[i]] == 0 and cur_mex > a[i]:
            cur_mex = a[i]

        another_have[a[i]] += 1
        while another_have[another_mex]:
            another_mex += 1

        if cur_mex == another_mex:
            print(2)
            print("1 " + str(i + 1))
            print(str(i + 2) + " " + str(n))
            return

    print(-1)


t = int(input())
for _ in range(t):
    solve()