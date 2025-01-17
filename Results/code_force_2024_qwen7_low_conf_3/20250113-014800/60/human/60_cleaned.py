def func_1(n, x, y, s):
    sequence = [x]
    current_sum = x
    for i in range(1, n):
        if current_sum + y <= s and (s - current_sum - y) % y == 0:
            sequence.append(sequence[-1] + y)
            current_sum += y
        else:
            sequence.append(sequence[-1] % y)
            current_sum += sequence[-1]
        if current_sum > s:
            return None
    if current_sum == s:
        return sequence
    else:
        return None
t = int(input())
for _ in range(t):
    (n, x, y, s) = map(int, input().split())
    result = func_1(n, x, y, s)
    if result:
        print('Yes')
        print(' '.join(map(str, result)))
    else:
        print('No')