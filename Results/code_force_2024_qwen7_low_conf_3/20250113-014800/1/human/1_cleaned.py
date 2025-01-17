def func_1():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        k = 2 * k
        a = list(map(int, input().split()))
        occ = [0] * (n + 1)
        for x in a:
            occ[x] += 1
        (g0, g1, g2) = ([], [], [])
        for i in range(1, n + 1):
            if occ[i] == 0:
                g0.append(i)
            elif occ[i] == 1:
                g1.append(i)
            else:
                g2.append(i)
        v = 0
        output = []
        for x in g2:
            if v < k:
                output.append(f'{x} {x}')
                v += 2
        for x in g1:
            if v < k:
                output.append(f'{x}')
                v += 1
        print(' '.join(output))
        v = 0
        output = []
        for x in g0:
            if v < k:
                output.append(f'{x} {x}')
                v += 2
        for x in g1:
            if v < k:
                output.append(f'{x}')
                v += 1
        print(' '.join(output))
if __name__ == '__main__':
    func_1()