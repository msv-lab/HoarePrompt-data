def func_1(n, x):
    count = 0
    k = 2
    while 2 * k - 2 <= n:
        cycle_length = 2 * k - 2
        position_in_cycle = (n - 1) % cycle_length + 1
        if position_in_cycle <= k:
            expected_number = position_in_cycle
        else:
            expected_number = 2 * k - position_in_cycle
        if expected_number == x:
            count += 1
        k += 1
    return count

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        index += 2
        results.append(func_1(n, x))
    for result in results:
        print(result)