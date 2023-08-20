def maximum_number_of_problems(n, difficulties):
    max_count = 1
    count = 1
    for i in range(1, n):
        if difficulties[i] <= 2 * difficulties[i-1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count

n = int(input())
difficulties = list(map(int, input().split()))
result = maximum_number_of_problems(n, difficulties)
print(result)