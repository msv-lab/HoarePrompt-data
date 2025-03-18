#State of the program right berfore the function call: n and k are integers such that 1 <= k <= n <= 200,000, and the lists lista_A and lista_B are lists of integers of length n, with each element in the range 1 <= a_i, b_i <= 10^9.
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
        
    #State: `n` and `k` remain unchanged, `lista_A` and `lista_B` remain unchanged, `soma_b` is the sum of the elements in `lista_B` from index `n-k` to `n-1` that are greater than or equal to the corresponding elements in `lista_A`, and `pref` is the sum of `soma_b` values and the corresponding elements in `lista_A` for each index `i` from 0 to `n-k-1` where `lista_A[i] < lista_B[i]`.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `n` and `k` remain unchanged, `lista_A` and `lista_B` remain unchanged, `soma_b` is the sum of the elements in `lista_B` from index `n-k` to `n-1`, `pref` remains unchanged, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for each index `i` from `n-k` to `n-1`.
    print(resultado)
    #This is printed: - The `print(resultado)` statement will print the minimum value of `pref + soma_b + lista_A[i]` for each index `i` from `n-k` to `n-1`.
    #
    #Since the exact values of `n`, `k`, `lista_A`, `lista_B`, and `pref` are not provided, we can only describe the output in terms of these variables.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It reverses both lists and then processes them to compute a value `resultado`. This value is the minimum of `pref + soma_b + lista_A[i]` for each index `i` from `n-k` to `n-1`, where `pref` is the sum of `soma_b` values and the corresponding elements in `lista_A` for indices from 0 to `n-k-1` where `lista_A[i] < lista_B[i]`, and `soma_b` is the sum of the elements in `lista_B` from index `n-k` to `n-1`. The function prints `resultado` and does not return any value. The function does not modify the input lists `lista_A` and `lista_B`.

#State of the program right berfore the function call: numero_testes is a non-negative integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: The loop has executed `numero_testes` times, and the value of `numero_testes` remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `numero_testes` from the user input, where `1 <= numero_testes <= 10^4`. The function then calls `func_1` exactly `numero_testes` times. After the function concludes, `numero_testes` remains unchanged, and the state of the program is as it was before the function call, except for any side effects caused by `func_1`. The overall purpose of the function is to execute `func_1` a specific number of times based on user input.

