def func_1(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
    max_score = 0
    for num in range(1, n + 1):
        if num in count_a:
            if count_a[num] == 2:
                max_score += 1
    return max_score
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = func_1(a, n)
    results.append(result)
for res in results:
    print(res)