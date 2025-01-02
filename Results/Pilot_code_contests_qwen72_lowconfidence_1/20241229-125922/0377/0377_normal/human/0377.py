n = int(input())
v = [float(x) for x in raw_input().split()]
v.sort()

def mean(a, b):
    return (a+b)/2

result = v[0]

for i in range(1, n):
    result = mean(result, v[i])

print(result)
