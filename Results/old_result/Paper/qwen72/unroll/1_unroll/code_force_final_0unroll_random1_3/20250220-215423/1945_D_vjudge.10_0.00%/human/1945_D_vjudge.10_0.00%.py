x = int(input())
custos = []
 
for i in range(x):
    custo = 0
    num_fila = 0
    max_p = 0
    a_values = []
    b_values = []
    nf = input().split()
    num_fila = int(nf[0])
    max_p = int(nf[1])
    a = input().split()
    b = input().split()
    for y in a:
        a_values.append(int(y))
    for y in b:
        b_values.append(int(y))
    for y in range(num_fila - 1, max_p - 1, -1):
        if a_values[y] < b_values[y]:
            custo += a_values[y]
        else:
            custo += b_values[y]
    for y in range(max_p - 1, 0, -1):
        if (a_values[y - 1] + b_values[y]) <= a_values[y]:
            custo += b_values[y]
            if y == 1:
                custo += a_values[0]
                break
        else:
            custo += a_values[y]
            break
    custos.append(custo)
    
for c in custos:
    print(c)