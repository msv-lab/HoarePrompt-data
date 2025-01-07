def func_1(n, m, A):
    operations = []
    B = [[0] * m for _ in range(n)]
    for i in range(n - 1):
        for j in range(m - 1):
            if A[i][j] == 1 and A[i][j + 1] == 1 and (A[i + 1][j] == 1) and (A[i + 1][j + 1] == 1):
                B[i][j] = B[i][j + 1] = B[i + 1][j] = B[i + 1][j + 1] = 1
                operations.append((i + 1, j + 1))
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return -1
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    A = []
    index = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            index += 1
        A.append(row)
    func_1(n, m, A)