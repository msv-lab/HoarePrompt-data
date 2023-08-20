def find_minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)
    
    if min_a != max_a:
        for D in range(max_a - min_a + 1):
            changes = 0
            for i in range(n):
                changes += (abs(a[i] - (min_a + D)) % D)
            if changes % 2 == 0:
                return D
                
    return -1


n = int(input())
a = list(map(int, input().split()))

result = find_minimum_D(n, a)

print(result)