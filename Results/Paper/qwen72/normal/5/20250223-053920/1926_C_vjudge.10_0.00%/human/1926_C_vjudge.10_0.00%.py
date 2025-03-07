def sum_of_digits(n):
    return sum(int(d) for d in str(n))
soma = 0
N = int(input())
 
for _ in range(N):
    n = int(input())
    for i in range(n):
        soma += sum_of_digits(i)
 
print(soma)