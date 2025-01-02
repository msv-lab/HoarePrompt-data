def func_1(x):
    if 2 == x or 3 == x:
        return True
    if 0 == x % 2:
        return False
    for i in range(3, x):
        if x < i * i:
            break
        if 0 == x % i:
            return False
    return True
n = int(raw_input())
cnt = 0
for i in range(n):
    num = int(raw_input())
    if func_1(num):
        cnt += 1
print(cnt)