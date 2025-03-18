def func_1(s, k, n):
    s1 = ''
    s2 = ''
    alphabet = {chr(i) for i in range(97, 97 + k)}
    for i in s:
        if i in alphabet:
            if len(alphabet) != 1:
                alphabet.remove(i)
            else:
                s2 += i
                alphabet = {chr(i) for i in range(97, 97 + k)}
            s1 += i
    r = len(s1) // k
    return (len(s1) >= n * k, s1[r * k:], s2)
t = int(input())
OUT = []
for _ in range(t):
    (n, k, m) = map(int, input().split())
    s = input()
    (b, s1, s2) = func_1(s, k, n)
    if not b:
        OUT.append('No')
        i = 97
        while i <= k + 97:
            if chr(i) not in s1:
                break
            i += 1
        be9i = chr(i) * (n - len(s2))
        OUT.append(s2 + be9i)
    else:
        OUT.append('Yes')
for i in OUT:
    print(i)