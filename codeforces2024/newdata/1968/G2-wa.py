def lcp_prefix(a, b):
    # Esta função calcula o comprimento do prefixo comum mais longo entre as strings a e b
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i

def compute_max_lcp_for_k(s, k):
    n = len(s)
    max_lcp = 0
    # Dividir a string em k substrings
    chunk_size = n // k
    for i in range(k):
        # Gerar as substrings para essa divisão
        start = i * chunk_size
        end = start + chunk_size if i != k - 1 else n
        substrings = [s[start:end]]
        # Calcular o máximo LCP para a divisão da string
        lcp_value = 0
        for j in range(i + 1, k):
            next_start = j * chunk_size
            next_end = next_start + chunk_size if j != k - 1 else n
            lcp_value = max(lcp_value, lcp_prefix(substrings[-1], s[next_start:next_end]))
        max_lcp = max(max_lcp, lcp_value)
    return max_lcp

# Leitura de entrada
t = int(input())  # Número de casos de teste
for _ in range(t):
    # Leitura dos parâmetros para cada caso de teste
    n, l, r = map(int, input().split())
    s = input().strip()

    # Para cada k no intervalo [l, r], calcula o valor de f_k
    results = []
    for k in range(l, r + 1):
        results.append(compute_max_lcp_for_k(s, k))

    # Imprimir os resultados para este caso de teste
    print(" ".join(map(str, results)))
