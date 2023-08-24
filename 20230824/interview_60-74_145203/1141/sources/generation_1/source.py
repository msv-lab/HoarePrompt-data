n, m = map(int, input().split())
s = input()

for _ in range(m):
    l, r, c_1, c_2 = input().split()
    l = int(l) - 1
    r = int(r) - 1

    for i in range(l, r+1):
        if s[i] == c_1:
            s = s[:i] + c_2 + s[i+1:]

print(s)