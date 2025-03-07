def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
for _ in range(int(input())):
    func_1()