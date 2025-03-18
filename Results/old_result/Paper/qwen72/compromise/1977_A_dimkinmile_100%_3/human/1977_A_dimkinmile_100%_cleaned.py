def func_1():
    (n, m) = map(int, input().split())
    if (n - m) % 2 == 0 and n - m >= 0:
        print('Yes')
    else:
        print('No')
kreker = int(input())
for i in range(kreker):
    func_1()