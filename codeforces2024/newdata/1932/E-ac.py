def solve(n, s):
    s = s[::-1]
    a = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        a[i] = a[i + 1] + int(s[i])
    
    res = []
    c = 0
    for i in range(n):
        c += a[i]
        res.append(str(c % 10))
        c //= 10  
    res.append(str(c))
    while res and res[-1] == '0':
        res.pop()

    res = ''.join(res[::-1])

    return res


test_cases = int(input())
ans = []
for _ in range(test_cases):
    n = int(input())
    number = input()
    ans.append(solve(n, number))

print("\n".join(map(str, ans)))


