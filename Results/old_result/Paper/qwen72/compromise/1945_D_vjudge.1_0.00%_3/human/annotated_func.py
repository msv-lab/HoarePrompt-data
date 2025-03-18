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
        
    #State: `soma_b` is the sum of the last `k` elements of `lista_B` that are greater than or equal to the corresponding elements in `lista_A`, and `pref` is the sum of all elements in `lista_A` that are less than the corresponding elements in `lista_B` before the last `k` elements, plus the sum of `soma_b` values accumulated during these iterations.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `soma_b` is the sum of the last `k` elements of `lista_B` that are greater than or equal to the corresponding elements in `lista_A`, plus the sum of the last `k` elements of `lista_B`. `pref` remains unchanged. `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for all `i` in the range `n - k` to `n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of `pref + soma_b + lista_A[i]` for all `i` in the range `n - k` to `n - 1`, and `soma_b` is the sum of the last `k` elements of `lista_B` that are greater than or equal to the corresponding elements in `lista_A`, plus the sum of the last `k` elements of `lista_B`)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It processes these lists to compute a result, which is the minimum value of the sum of a prefix sum of `lista_A` and a suffix sum of `lista_B` over the last `k` elements. Specifically, it calculates the sum of elements in `lista_A` that are less than the corresponding elements in `lista_B` before the last `k` elements, and the sum of the last `k` elements of `lista_B`. The final result is the minimum value of this sum plus the corresponding element in `lista_A` for the last `k` elements. The function prints this result.

#State of the program right berfore the function call: numero_testes is a positive integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: The loop has executed `func_1()` `numero_testes` times, and `numero_testes` remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer from the user input, which is expected to be a positive integer between 1 and 10,000 inclusive. It then calls the function `func_1` that many times. The function does not return any value, and the input integer `numero_testes` remains unchanged after the function execution.

