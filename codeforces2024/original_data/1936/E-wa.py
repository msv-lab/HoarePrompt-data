MOD = 998244353

def solve_permutation_problem(t, test_cases):
    results = []
    for n, p in test_cases:
        # Paso 1: Crear un arreglo de máximos parciales de p
        max_p = [0] * n
        max_p[0] = p[0]
        
        # Calcular max(p_1, p_2, ..., p_i) para cada i
        for i in range(1, n):
            max_p[i] = max(max_p[i - 1], p[i])
        
        # Paso 2: Comprobar cuántas posibles permutaciones q satisfacen las condiciones
        count = 0
        max_value = max_p[-1]  # El máximo global
        
        # Estrategia: Verificar la condición de cada posición
        for i in range(n):
            if p[i] == max_value and max_p[i] == max_value:
                count += 1  # Esta es una posible posición donde q puede coincidir
        
        # Si no encontramos ninguna posición válida, ponemos 1 como mínimo
        if count == 0:
            count = 1
        
        # Paso 3: Añadir el resultado módulo 998244353
        results.append(count % MOD)
    
    return results

# Ejemplo de entrada para 6 casos de prueba
t = 6
test_cases = [
    (2, [2, 1]),
    (3, [1, 2, 3]),
    (3, [3, 1, 2]),
    (4, [2, 4, 1, 3]),
    (5, [3, 5, 1, 4, 2]),
    (15, [6, 13, 2, 8, 7, 11, 1, 3, 9, 15, 4, 5, 12, 10, 14])
]

# Llamar a la función con los datos de prueba
results = solve_permutation_problem(t, test_cases)

# Imprimir los resultados
for result in results:
    print(result)
