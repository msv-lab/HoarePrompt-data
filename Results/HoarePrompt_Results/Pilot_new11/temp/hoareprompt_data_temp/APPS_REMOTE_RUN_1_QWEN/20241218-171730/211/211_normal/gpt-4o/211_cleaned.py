n = int(input())
A = list(map(int, input().split()))
total_sum = sum(A)
if total_sum != 0:
    print('YES')
    print('1')
    print('1', n)
else:
    for i in range(n):
        if A[i] != 0:
            print('YES')
            print('2')
            print('1', i + 1)
            print(i + 2, n)
            break
    else:
        print('NO')