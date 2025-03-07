def func_1(a, b, c):
    return a + b > c and a + c > b and (b + c > a)

def func_2(n, na, nb, nc, numbers):
    numbers.sort(reverse=True)
    (group_a, group_b, group_c) = ([], [], [])
    (sum_a, sum_b, sum_c) = (0, 0, 0)

    def distribute_number(num):
        nonlocal sum_a, sum_b, sum_c
        if len(group_a) < na or (len(group_a) == na and sum_a <= min(sum_b, sum_c)):
            group_a.append(num)
            sum_a += num
        elif len(group_b) < nb or (len(group_b) == nb and sum_b <= min(sum_a, sum_c)):
            group_b.append(num)
            sum_b += num
        else:
            group_c.append(num)
            sum_c += num
    for num in numbers:
        distribute_number(num)
    if func_1(sum_a, sum_b, sum_c):
        return ('YES', group_a, group_b, group_c)
    else:
        return 'NO'
t = int(input())
out = []
for _ in range(t):
    (n, na, nb, nc) = map(int, input().split())
    x = list(map(int, input().split()))
    result = func_2(n, na, nb, nc, x)
    if result == 'NO':
        out.append('NO')
    else:
        out.append(['YES', result[1], result[2], result[3]])
for result in out:
    if result == 'NO':
        print(result)
    else:
        print(result[0])
        for group in result[1:]:
            print(' '.join(map(str, group)))