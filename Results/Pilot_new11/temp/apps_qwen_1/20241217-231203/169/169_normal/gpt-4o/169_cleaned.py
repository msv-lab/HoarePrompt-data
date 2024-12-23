n = int(input())
s = input()
stones = 0
for operation in s:
    if operation == '+':
        stones += 1
    elif operation == '-':
        stones = max(0, stones - 1)
print(stones)