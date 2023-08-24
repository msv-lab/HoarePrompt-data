N = int(input())
offers = list(map(int, input().split()))

offers.sort()
cookies = 0

for i in range(N-1):
    if offers[i+1] - offers[i] >= 4*10**5:
        cookies += 3

print(cookies)