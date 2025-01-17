m, s = map(int, input().split())

def min_num(m, s):
    if s == 0:
        if m > 1:
            return -1
        else:
            return 0
    if s > 9 * m:
        return -1
    num = ''
    for _ in range(m):
        if s > 9:
            num += '9'
            s -= 9
        else:
            num += str(s)
            s = 0
    return int(num)

def max_num(m, s):
    if s == 0:
        if m > 1:
            return -1
        else:
            return 0
    if s > 9 * m:
        return -1
    num = ''
    for _ in range(m - 1):
        if s > 9:
            num += '9'
            s -= 9
        else:
            num += str(s)
            s = 0
    num += str(s)
    return int(num)

min_num_val = min_num(m, s)
max_num_val = max_num(m, s)

if min_num_val == -1 or max_num_val == -1:
    print(-1, -1)
else:
    print(min_num_val, max_num_val)
