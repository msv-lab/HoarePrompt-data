def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(a, b):
    return a * b // func_1(a, b)
(a, b) = map(int, input().split())
k = 0
min_lcm = func_2(a, b)
while True:
    if func_2(a + k, b + k) < min_lcm:
        min_lcm = func_2(a + k, b + k)
    else:
        break
    k += 1
print(k - 1)