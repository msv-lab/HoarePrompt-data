S = map(int, raw_input().split())
N = S[0]
X = S[1]

m = []
for i in range(N):
    m.append(int(raw_input()))

X -= sum(m)

print(len(m) + X // sorted(m)[0])
