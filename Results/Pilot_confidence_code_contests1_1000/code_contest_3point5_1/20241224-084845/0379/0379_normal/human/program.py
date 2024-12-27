N = int(raw_input())
A = map(int, raw_input().split())

average = sum(A)/float(N)

diff = max(A)
index = None

for i, a in enumerate(A):
    if abs(a-average) < diff:
        index = i
        diff = abs(a-average)
print(index)
