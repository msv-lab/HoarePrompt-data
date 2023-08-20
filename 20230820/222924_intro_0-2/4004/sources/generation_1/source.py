def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return 0
    elif (max_a - min_a) % (n-1) != 0:
        return -1
    else:
        D = (max_a - min_a) // (n-1)
        for i in range(n):
            if a[i] - min_a > D or (a[i] - min_a) % D != 0:
                return -1
        return D

n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)
print(result)