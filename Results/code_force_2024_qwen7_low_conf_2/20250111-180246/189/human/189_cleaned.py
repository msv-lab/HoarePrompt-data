def func_1(n):
    points = []
    for i in range(n):
        x = i + 1
        y = i * 2 % n + 1
        points.append((x, y))
    return points

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(t):
        n = int(data[i + 1])
        result = func_1(n)
        results.append(result)
    for result in results:
        for (x, y) in result:
            print(x, y)
if __name__ == '__main__':
    func_2()