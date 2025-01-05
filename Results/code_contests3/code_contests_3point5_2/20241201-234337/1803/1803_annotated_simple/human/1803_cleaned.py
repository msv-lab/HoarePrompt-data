Cadena = raw_input()
Arreglo = []
k = 1
while len(Cadena) > k and len(Cadena) > 2:
    Arreglo = Arreglo + [Cadena[k]]
    k = k + 3
print(len(list(set(Arreglo))))