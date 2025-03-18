def is_undulating(n):
    n = str(n)
    undulating = True
    for i in range(1, len(n) - 1):
        if (n[i-1] < n[i] and n[i] < n[i+1]) or (n[i-1] > n[i] and n[i] > n[i+1]):
            pass
        else:
            undulating = False
            break
    return undulating
