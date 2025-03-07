def func_1(a, b):
    return 'yes' if b % 2 == 0 else 'no'
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    print(func_1(a, b))