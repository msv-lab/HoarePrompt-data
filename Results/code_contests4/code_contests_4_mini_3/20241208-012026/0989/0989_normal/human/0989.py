from sys import stdin

n, s = int(input()), stdin.readline().strip()
if len(s) % n:
    tem = '1' + '0' * (n - 1)
    print(tem * (len(s) // n + 1))
elif s[:n] == '9' * n:
    ans1, ans2 = '9' * len(s), '1' + '0' * n
    print(ans1 if ans1 > s else ans2 * (len(s) // n))
else:
    ans1, tem = s[:n] * (len(s) // n), list(s[:n])
    for i in range(n - 1, -1, -1):
        if tem[i] != '9':
            tem[i] = str(int(tem[i]) + 1)
            break
        tem[i] = '0'

    ans2 = ''.join(tem) * (len(s) // n)
    print(ans1 if ans1 > s else ans2)
