def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        last_year = a[0]
        for i in range(1, n):
            next_year = (last_year + 1 + a[i] - 1) // a[i] * a[i]
            last_year = next_year
        results.append(str(last_year))
    sys.stdout.write('\n'.join(results) + '\n')
if __name__ == '__main__':
    func_1()