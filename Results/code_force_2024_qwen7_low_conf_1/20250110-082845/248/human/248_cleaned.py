MOD = 999999893

def func_1(a, p):
    return pow(a, p - 2, p)

def func_2(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        return 714285638
input = sys.stdin.read
data = input().split()
t = int(data[0])
results = []
for i in range(1, t + 1):
    N = int(data[i])
    results.append(func_2(N))
for result in results:
    print(result)