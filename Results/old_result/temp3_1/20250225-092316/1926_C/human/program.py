soma = 0
for i in range(13):
    soma += func_1(i)
print(soma)

def func_1(n):
    return sum((int(d) for d in str(n)))

