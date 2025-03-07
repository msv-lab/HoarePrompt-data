#State of the program right berfore the function call: n is a positive integer representing the number of people in the queue besides Kirill, and k is a positive integer such that 1 <= k <= n. lista_A and lista_B are lists of integers of length n, where each element in lista_A and lista_B is a positive integer representing the cost a_i and b_i respectively for each person in the queue.
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
        
    #State: `n` is the first integer from the input, `k` is the second integer from the input, `lista_A` is a list of integers of length `n` representing the cost `a_i` for each person in the queue, but in reverse order, `lista_B` is a list of integers of length `n` representing the cost `b_i` for each person in the queue, but now in the reversed order, `soma_b` is the sum of `lista_B[i]` for all `i` where `lista_A[i] >= lista_B[i]` and no `lista_A[j] < lista_B[j]` has occurred after `i` that would reset `soma_b`, `pref` is the accumulated sum as described in the loop logic.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `n` is the first integer from the input, `k` is the second integer from the input, `lista_A` is a list of integers of length `n` representing the cost `a_i` for each person in the queue, but in reverse order, `lista_B` is a list of integers of length `n` representing the cost `b_i` for each person in the queue, but now in the reversed order, `soma_b` is the sum of `lista_B[i]` for all `i` from `n - k` to `n - 1`, `pref` is the accumulated sum as described in the loop logic, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for all `i` from `n - k` to `n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for all i from n - k to n - 1)
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It calculates and prints the minimum value of a specific expression involving elements from `lista_A` and `lista_B` based on the given constraints.

#State of the program right berfore the function call: numero_testes is an integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: The loop has executed `numero_testes` times, and `func_1()` has been called `numero_testes` times. The state of any variables not mentioned in the loop head or body remains unchanged.
#Overall this is what the function does:The function `func_2` reads an integer `numero_testes` from the input, which represents the number of tests to be performed. It then calls `func_1` exactly `numero_testes` times. The function does not accept any parameters and does not return any value. The state of the program after it concludes is that `func_1` has been executed the specified number of times, but the specific effects of these calls on the program's state are not detailed in the provided code.

