t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print('NO')
    else:
        print('YES')
        pattern = []
        for i in range(n // 2):
            pattern.append('AB'[i % 2])
            pattern.append('AB'[i % 2 ^ 1])
        print(''.join(pattern))