n, m = map(int, input().split())
s = input()

for _ in range(m):
    l, r, c_1, c_2 = input().split()
    l = int(l) - 1
    r = int(r) - 1

    new_s = s
    for i in range(l, r+1):
        if new_s[i] == c_1:
            new_s = new_s[:i] + c_2 + new_s[i+1:]

    s = new_s

print(s)