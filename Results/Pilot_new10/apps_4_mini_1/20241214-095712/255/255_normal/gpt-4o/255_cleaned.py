n = int(input())
s = input()
operations = 1
for i in range(1, n):
    if s[i] != s[i - 1]:
        operations += 1
print(operations)