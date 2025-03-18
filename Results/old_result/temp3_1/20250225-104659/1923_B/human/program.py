if __name__ == '__main__':
    func_2()

def func_1():
    try:
        (n, k) = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        for i in range(n):
            x = int(input())
            b[abs(x)] += a[i]
        r = 0
        for i in range(1, n + 1):
            r += k
            if r < b[i]:
                print('NO')
                return
            r -= b[i]
        print('YES')
    except ValueError:
        print('Invalid input format')

def func_2():
    try:
        t = int(input())
        for _ in range(t):
            func_1()
    except ValueError:
        print('Invalid input format')

