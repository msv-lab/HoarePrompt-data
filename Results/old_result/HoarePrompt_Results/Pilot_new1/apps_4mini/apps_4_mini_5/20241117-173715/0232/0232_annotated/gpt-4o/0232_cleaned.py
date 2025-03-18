def func_1(n, m, colors, k):
    from collections import defaultdict
    desired_counts = dict(zip(range(1, m + 1), k))
    current_counts = defaultdict(int)
    left = 0
    for right in range(n):
        current_counts[colors[right]] += 1
        while all((current_counts[color] >= desired_counts[color] for color in desired_counts)):
            if all((current_counts[color] == desired_counts[color] for color in desired_counts)):
                return 'YES'
            current_counts[colors[left]] -= 1
            left += 1
    return 'NO'
(n, m) = map(int, input().split())
colors = list(map(int, input().split()))
k = list(map(int, input().split()))
print(func_1(n, m, colors, k))