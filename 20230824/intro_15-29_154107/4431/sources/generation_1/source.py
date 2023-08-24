n, k = map(int, input().split())
s = input()
available_letters = input().split()

count = 0

for i in range(n):
    if s[i] not in available_letters:
        continue
    count += 1
    for j in range(i+1, n):
        if s[j] not in available_letters:
            break
        count += 1

print(count)