#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 200,000, lista_A and lista_B are lists of integers of length n where each element is in the range [1, 10^9].
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
        
    #State: `n` is greater than `k`, `i` is `n - k - 1`, `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 200,000, `lista_A` is a reversed list of integers of length `n`, `lista_B` is a reversed list of integers of length `n`. `pref` is the sum of all elements from `lista_A` that were less than their corresponding elements in `lista_B` during the loop, plus the cumulative `soma_b` values added to it when `lista_A[i] < lista_B[i]`. `soma_b` is the sum of all elements from `lista_B` that were greater than or equal to their corresponding elements in `lista_A` during the loop.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: After the loop has executed all iterations, `i` is `n - 1`, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for all `i` from `n - k - 1` to `n - 1`, and `soma_b` is the sum of all elements from `lista_B` from index `n - k - 1` to `n - 1`. The other variables (`n`, `k`, `lista_A`, `lista_B`, `pref`) remain unchanged.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of `pref + soma_b + lista_A[i]` for all `i` from `n - k - 1` to `n - 1`)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It reverses both lists and calculates a value `resultado` which is the minimum sum of elements from `lista_A` and `lista_B` under specific conditions. Specifically, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for all `i` from `n - k - 1` to `n - 1`, where `pref` and `soma_b` are computed based on the comparison of elements in `lista_A` and `lista_B`. Finally, the function prints the calculated `resultado`.

#State of the program right berfore the function call: numero_testes is a positive integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is a positive integer such that 0 < `numero_testes` <= 10^4, and the loop has completed all `numero_testes` iterations.
#Overall this is what the function does:The function `func_2` reads an integer `numero_testes` from the user input, where `1 <= numero_testes <= 10^4`. It then iterates `numero_testes` times, calling the function `func_1()` in each iteration. After the function completes, `numero_testes` remains a positive integer within the specified range, and `func_1()` has been called `numero_testes` times. The function does not return any value.

