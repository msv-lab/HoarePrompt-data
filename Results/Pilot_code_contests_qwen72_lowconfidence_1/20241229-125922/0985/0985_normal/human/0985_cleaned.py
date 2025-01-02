def func_1():
    (H, W) = map(int, raw_input().split())
    a = []
    result = []
    for i in range(H):
        a.append(map(int, raw_input().split()))
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue
            elif j + 1 < W:
                result.append([i + 1, j + 1, i + 1, j + 2])
                a[i][j] = a[i][j] - 1
                a[i][j + 1] = a[i][j + 1] + 1
            elif j + 1 == W and i + 1 < H:
                result.append([i + 1, j + 1, i + 2, j + 1])
                a[i][j] = a[i][j] - 1
                a[i + 1][j] = a[i + 1][j] + 1
    print(len(result))
    for i in range(len(result)):
        for j in range(len(result[i])):
            if j == len(result[i]) - 1:
                print(result[i][j])
            else:
                (print(result[i][j]),)
if __name__ == '__main__':
    func_1()