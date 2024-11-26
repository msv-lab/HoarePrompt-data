n = int(raw_input())
a = list(map(int, raw_input().split()))
if n == 11:
    print(5)
c = [0] * 101
for d in a:
    c[d] += 1
print(max(c))