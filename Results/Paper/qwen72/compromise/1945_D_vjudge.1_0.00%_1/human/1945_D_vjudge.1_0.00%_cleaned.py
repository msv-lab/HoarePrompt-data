def func_1():
    (n, k) = map(int, input().split())
    lista_A = list(map(int, input().split()))
    lista_A.reverse()
    lista_B = list(map(int, input().split()))
    lista_B.reverse()
    soma_b = 0
    pref = 0
    for i in range(n - k):
        if lista_A[i] < lista_B[i]:
            pref += soma_b
            pref += lista_A[i]
            soma_b = 0
        else:
            soma_b += lista_B[i]
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        soma_b += lista_B[i]
    print(resultado)

def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()