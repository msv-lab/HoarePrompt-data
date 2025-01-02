N = input()
n = []
for i in range(N):
    n.append(raw_input())
M = input()
m = []
for i in range(M):
    m.append(raw_input())

result = [n.count(a) - m.count(a) for a in n]
max_ = max(result)
if max_ < 0:
    print(0)
else:
    print(max_)