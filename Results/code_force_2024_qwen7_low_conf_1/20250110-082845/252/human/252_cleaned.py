def func_1():
    (n, k) = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(map(int, input().split()))
    put_all_on_right = [0] * (n + 1)
    for i in range(n):
        put_all_on_right[abs(x[i])] += v[i]
    my_power = k
    for i in range(1, n + 1):
        if my_power < put_all_on_right[i]:
            print('NO')
            return
        my_power -= put_all_on_right[i]
        my_power += k
    print('YES')

def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
if __name__ == '__main__':
    func_2()