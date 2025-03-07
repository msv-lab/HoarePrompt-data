t = int(input())  # Número de casos de prueba
 
for _ in range(t):
    a, b = map(int, input().split())  # Leer las dimensiones del rectángulo
    
    # Si cualquiera de las dimensiones es par
    if a % 2 == 0 or b % 2 == 0:
        # Hacer un corte en la dimensión par
        if a % 2 == 0:  # Dividir a en dos partes si es par
            a1, a2 = a // 2, a // 2
            if a1 != b:  # Verificar que no se forme un cuadrado al dividir
                print("Yes")
                continue
        
        if b % 2 == 0:  # Dividir b en dos partes si es par
            b1, b2 = b // 2, b // 2
            if b1 != a:  # Verificar que no se forme un cuadrado al dividir
                print("Yes")
                continue
 
        # Si no se puede formar un nuevo rectángulo
        print("No")
    else:
        # Si ambos lados son impares, no se puede formar otro rectángulo
        print("No")