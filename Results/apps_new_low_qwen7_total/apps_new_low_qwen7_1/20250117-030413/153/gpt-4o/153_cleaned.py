def func_1(n, m, k, x, s, a, b, c, d):
    min_time = n * x
    for i in range(k):
        if d[i] <= s:
            remaining_potions = max(0, n - c[i])
            time_with_spell = remaining_potions * x
            min_time = min(min_time, time_with_spell)
    for i in range(m):
        if b[i] <= s:
            time_with_spell = n * a[i]
            min_time = min(min_time, time_with_spell)
    for i in range(m):
        if b[i] <= s:
            remaining_manapoints = s - b[i]
            for j in range(k):
                if d[j] <= remaining_manapoints:
                    remaining_potions = max(0, n - c[j])
                    time_with_both_spells = remaining_potions * a[i]
                    min_time = min(min_time, time_with_both_spells)
                else:
                    break
    return min_time
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    x = int(data[3])
    s = int(data[4])
    a = list(map(int, data[5:5 + m]))
    b = list(map(int, data[5 + m:5 + 2 * m]))
    c = list(map(int, data[5 + 2 * m:5 + 2 * m + k]))
    d = list(map(int, data[5 + 2 * m + k:5 + 2 * m + 2 * k]))
    result = func_1(n, m, k, x, s, a, b, c, d)
    print(result)