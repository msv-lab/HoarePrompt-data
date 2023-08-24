N = int(input())
offers = list(map(int, input().split()))

offers.sort()
cookies = 0
end_time = 0

for i in range(N):
    if offers[i] >= end_time:
        cookies += 1
        end_time = offers[i] + 4*10**5

earned_cookies = cookies * 1
print(earned_cookies)