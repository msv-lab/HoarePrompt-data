# Read inputs
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Check if war will break out
if X < min(y) <= Y and max(x) < min(y):
    print("No War")
else:
    print("War")