import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
arr = list(map(int, input().split()))

k = 0
ans = [arr[0]]
for i in range(1, n):
    if gcd(arr[i-1], arr[i]) != 1:
        k += 1
        for j in range(1, 10**9 + 1):
            if gcd(arr[i-1], j) == 1 and gcd(j, arr[i]) == 1:
                ans.append(j)
                break
    ans.append(arr[i])

print(k)
print(' '.join(map(str, ans)))
