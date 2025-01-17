n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(n):
    if a[i] == 0:
        a[i] = b.pop(0)

for i in range(1, n):
    if a[i] <= a[i-1]:
        print("Yes")
        exit()

print("No")
