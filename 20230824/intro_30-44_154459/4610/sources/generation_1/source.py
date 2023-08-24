def minimum_rewrite(N, K, balls):
    freq = {}
    for ball in balls:
        if ball in freq:
            freq[ball] += 1
        else:
            freq[ball] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1])

    count = 0
    i = 0
    while len(sorted_freq) > K:
        count += sorted_freq[i][1]
        sorted_freq.pop(i)
        i += 1

    return count

# Read input
N, K = map(int, input().split())
balls = list(map(int, input().split()))

# Call the function and print the result
result = minimum_rewrite(N, K, balls)
print(result)