def func_1(expression, length):
    count = 0
    balance = 0
    for char in expression:
        if char == '+':
            balance += 1
        elif char == '-':
            balance -= 1
        if balance < 0:
            count += 1
            balance = 0
    return count + (balance > 0)
t = int(input())
for _ in range(t):
    length = int(input())
    expression = input().strip()
    parts = expression.split('-')
    result_length = sum((len(part) for part in parts))
    print(func_1(expression, result_length))