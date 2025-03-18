n = int(input())
s = input()
b = list(map(int, input().split()))

s_sorted = sorted(s)
b_sorted = sorted(b, reverse=True)

t = ''
for i in range(n//2):
    t += s_sorted[i]
    t += s_sorted[n-i-1]

max_beauty = 0
for i in range(n):
    if s[i] == t[i]:
        max_beauty += b_sorted[i]

print(max_beauty)
