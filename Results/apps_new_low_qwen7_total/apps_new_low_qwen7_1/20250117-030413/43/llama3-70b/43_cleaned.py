n = int(input())
s = input()
count = 0
for i in range(2 ** n):
    t = bin(i)[2:].zfill(n)
    if all((t[i:i + len(s)] == s or t[i + len(s):] + t[:i] == s for i in range(n))):
        count += 1
print(count)