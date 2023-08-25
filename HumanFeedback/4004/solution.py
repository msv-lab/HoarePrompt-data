def solve_problem():
    n = int(input())
    a = set(map(int, input().split()))

    l = len(a)
    if l > 3:
        return '-1'
    elif l == 1:
        return '0'
    elif l == 2:
        return str(max(a) - min(a)) if (max(a) - min(a)) % 2 != 0 else str((max(a) - min(a)) // 2)
    else:
        a = sorted(a)
        return str(a[1] - a[0]) if a[1] - a[0] == a[2] - a[1] else '-1'

print(solve_problem())