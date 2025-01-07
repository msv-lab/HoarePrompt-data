n = int(input())
max_9s = 0
while (n + 1) % 10 == 0:
    max_9s += 1
    n //= 10
pairs = (n + 1) * max_9s
print(pairs)