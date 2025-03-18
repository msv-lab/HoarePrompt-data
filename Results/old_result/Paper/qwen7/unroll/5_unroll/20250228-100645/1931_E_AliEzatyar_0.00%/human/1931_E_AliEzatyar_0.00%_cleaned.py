n_test = int(input())
answers = [None] * n_test

def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
    return counter
for test in range(n_test):
    (n, m) = tuple(map(int, input().split()))
    array = input().split()
    total_digits = 0
    zeros = []
    for item in array:
        total_digits += len(item)
        if func_1(item) > 0:
            zeros.append(func_1(item))
    zeros = sorted(zeros, reverse=True)
    subtract_zero = 0
    for i in range(0, len(zeros), 2):
        subtract_zero += zeros[i]
    if abs(total_digits - subtract_zero) >= m + 1:
        answers[test] = 'Sashah'
    else:
        answers[test] = 'Anna'
for answer in answers:
    print(answer)