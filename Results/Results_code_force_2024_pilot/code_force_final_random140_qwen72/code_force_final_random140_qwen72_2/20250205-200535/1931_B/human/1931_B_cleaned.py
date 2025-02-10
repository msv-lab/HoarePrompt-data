def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        if all((arr[i] <= arr[i + 1] for i in range(n - 1))):
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    func_1()