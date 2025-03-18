#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n. lista_A and lista_B are lists of integers of length n, where each element in lista_A and lista_B is between 1 and 10^9 inclusive.
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
        
    #State: `n` and `k` remain unchanged; `lista_A` and `lista_B` remain unchanged; `soma_b` is the sum of the last consecutive elements of `lista_B` where `lista_A[i]` was not less than `lista_B[i]`; `pref` is the accumulated sum from the loop steps.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `n` and `k` remain unchanged; `lista_A` and `lista_B` remain unchanged; `soma_b` is the sum of the last `k` elements of `lista_B`; `pref` remains unchanged; `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for `i` in the range from `n - k` to `n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for i in the range from n - k to n - 1)
#Overall this is what the function does:The function reads two integers `n` and `k` (with `1 <= k <= n`) and two lists of integers `lista_A` and `lista_B` of length `n`, where each element is between 1 and 10^9. It calculates and prints the minimum value of the expression `pref + soma_b + lista_A[i]` for `i` ranging from `n - k` to `n - 1`, where `pref` and `soma_b` are computed based on the conditions specified in the code.

#State of the program right berfore the function call: numero_testes is an integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` retains its initial value.
#Overall this is what the function does:The function `func_2` reads an integer `numero_testes` from the input, which represents the number of test cases to process. It then iterates `numero_testes` times, calling `func_1()` in each iteration. The function does not return any value and does not modify the input `numero_testes`.

