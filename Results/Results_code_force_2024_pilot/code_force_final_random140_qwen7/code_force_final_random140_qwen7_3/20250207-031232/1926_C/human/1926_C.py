def sum_of_digits(n):
    return sum(int(d) for d in str(n))
soma = 0
for i in range(13):
    soma += sum_of_digits(i)
 
print(soma)