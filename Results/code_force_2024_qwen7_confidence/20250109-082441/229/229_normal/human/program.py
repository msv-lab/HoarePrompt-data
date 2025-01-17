def min_operations(a, b):
    diff = [b[i] - a[i] for i in range(len(a))]
    count = 0

    for d in diff:
        if d > 0:
            count += d
        elif d < 0:
            count -= d

    return count