vector1 = [[0, -1], [1, 0], [0, 1], [-1, 0]]
vector2 = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]

def func_1():
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        (x, y) = S[-1]
        if s == '0':
            x += 1
        else:
            y += 1
        S.append([x, y])
    ans = -1
    for i in range(n + 1):
        left = S[i][0]
        lsum = i
        right = S[-1][1] - S[i][1]
        rsum = n - i
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) < abs(n / 2 - ans):
            ans = i
    print(ans)

def func_2():
    for _ in range(int(input())):
        func_1()
if __name__ == '__main__':
    func_2()