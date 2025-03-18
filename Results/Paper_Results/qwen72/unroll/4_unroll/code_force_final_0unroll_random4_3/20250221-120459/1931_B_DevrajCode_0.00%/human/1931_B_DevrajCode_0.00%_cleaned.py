def func_1(n, a):
    total_water = sum(a)
    if total_water % n != 0:
        return 'No'
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        if container < 0:
            return 'No'
    return 'Yes'
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))
print(func_1(n, a))