def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        num_up_coins = s.count('U')
        if num_up_coins % 2 == 1:
            results.append('YES')
        else:
            results.append('NO')
    for result in results:
        print(result)