n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count_a = [0] * 6
count_b = [0] * 6
for i in a:
    count_a[i] += 1
for i in b:
    count_b[i] += 1
ans = 0
for i in range(1, 6):
    ans += abs(count_a[i] - count_b[i])
print(ans // 2)