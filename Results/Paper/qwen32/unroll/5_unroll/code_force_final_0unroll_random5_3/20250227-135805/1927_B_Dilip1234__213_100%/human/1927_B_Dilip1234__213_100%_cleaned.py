def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
    return s
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(func_1(n, a))