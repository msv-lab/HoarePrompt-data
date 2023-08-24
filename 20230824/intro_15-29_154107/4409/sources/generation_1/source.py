def minimum_operations(n, a):
    operations = []
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
            if a[i] < a[i+1]:
                a[i] = a[i] + abs(a[i] - a[i+1])
                operations.append((1, i+1, i+2))
            else:
                a[i] = a[i] - abs(a[i] - a[i+1])
                operations.append((2, i+1, i+2))
    return count, operations

n = int(input())
a = list(map(int, input().split()))

count, operations = minimum_operations(n, a)

print(count)
for operation in operations:
    print(*operation)