n = int(input())
k = input()
x = 0
for i, c in enumerate(reversed(k)):
    x += int(c) * (n ** i)
print(x)
