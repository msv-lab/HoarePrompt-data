def func_1(n):
    return sum((int(d) for d in str(n)))
soma = 0
N = int(input())
for _ in range(N):
    n = int(input())
    for i in range(n):
        soma += func_1(i)
print(soma)