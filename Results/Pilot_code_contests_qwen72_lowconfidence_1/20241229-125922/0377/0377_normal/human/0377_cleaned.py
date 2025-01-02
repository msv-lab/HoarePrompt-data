n = int(input())
v = [float(x) for x in raw_input().split()]
v.sort()

def func_1(a, b):
    return (a + b) / 2
result = v[0]
for i in range(1, n):
    result = func_1(result, v[i])
print(result)