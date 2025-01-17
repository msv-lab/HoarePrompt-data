t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    max_sum = total_sum

    for j in range(n):
        current_negation_sum = 0
        for k in range(j, n):
            current_negation_sum += -arr[k]
            new_sum = total_sum - sum(arr[j:k + 1]) + current_negation_sum
            max_sum = max(max_sum, new_sum)

    print(max_sum)
