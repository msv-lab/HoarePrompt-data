N = int(raw_input())
X = map(int, raw_input().split())

for i in range(N):
    print(sorted(X[:i] + X[i+1:])[(N-1)/2])
