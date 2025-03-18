#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 200,000. lista_A and lista_B are lists of integers of length n, where each element a_i and b_i satisfies 1 <= a_i, b_i <= 10^9.
def func_1():
    n, k = map(int, input().split())
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
        
    #State: `n` and `k` remain unchanged. `lista_A` and `lista_B` remain unchanged. `soma_b` is the sum of elements in `lista_B` from index `k` to `n-1` that are not less than the corresponding elements in `lista_A`. `pref` is the sum of `soma_b` and the elements in `lista_A` from index `0` to `n-k-1` that are less than the corresponding elements in `lista_B`.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `n` and `k` remain unchanged, `lista_A` and `lista_B` remain unchanged, `soma_b` is the sum of elements in `lista_B` from index `k` to `n-1`, `pref` is the sum of `soma_b` and the elements in `lista_A` from index `0` to `n-k-1` that are less than the corresponding elements in `lista_B`, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for `i` in the range from `n-k` to `n-1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + lista_A[i] for i in the range from n-k to n-1, and pref is the sum of soma_b and the elements in lista_A from index 0 to n-k-1 that are less than the corresponding elements in lista_B, and soma_b is the sum of elements in lista_B from index k to n-1)
#Overall this is what the function does:The function `func_1` reads three lines of input: the first line contains two integers `n` and `k` (where 1 <= k <= n <= 200,000), the second line contains a list of `n` integers `lista_A` (where each element satisfies 1 <= a_i <= 10^9), and the third line contains a list of `n` integers `lista_B` (where each element satisfies 1 <= b_i <= 10^9). It then reverses both `lista_A` and `lista_B`. The function calculates a value `resultado` which is the minimum value of `pref + soma_b + lista_A[i]` for `i` in the range from `n-k` to `n-1`, where `pref` is the sum of elements in `lista_A` from index `0` to `n-k-1` that are less than the corresponding elements in `lista_B`, and `soma_b` is the sum of elements in `lista_B` from index `k` to `n-1`. Finally, the function prints `resultado`. The function does not return any value.

#State of the program right berfore the function call: numero_testes is a positive integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: The value of `numero_testes` remains unchanged, and the loop has executed `func_1` exactly `numero_testes` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `numero_testes` from user input, where `1 <= numero_testes <= 10^4`. The function then executes `func_1` exactly `numero_testes` times. After the function concludes, the value of `numero_testes` remains unchanged, and the program state reflects that `func_1` has been called the specified number of times.

