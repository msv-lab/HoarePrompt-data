def func_1():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    max_ones = n * (n + 1) // 2
    if k > max_ones:
        print(-1)
        return
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        if k <= 0:
            break
        matrix[i][i] = 1
        k -= 1
        for j in range(i + 1, n):
            if k <= 0:
                break
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            elif k == 1:
                matrix[i][j] = 1
                k -= 1
    for row in matrix:
        print(' '.join(map(str, row)))
if __name__ == '__main__':
    func_1()