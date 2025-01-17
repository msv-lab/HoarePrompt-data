n = int(input())
a = list(map(int, input().split()))
s = input()

possible = True
for i in range(n-1):
    if a[i] > a[i+1] and s[i] == '0':
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")
