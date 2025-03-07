#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 200,000, lista_A and lista_B are lists of integers of length n where 1 ≤ a_i, b_i ≤ 10^9, and both lists have been reversed.
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
        
    #State: `n` is greater than `k`, `i` is `n - k - 1`, `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 200,000, `lista_B` is a list of integers of length n where 1 ≤ b_i ≤ 10^9, and `lista_B` is in its original order, `lista_A` is a list of integers provided by the user input and has been reversed, `soma_b` is the sum of the last `n - k - 1` elements of `lista_B` that were not less than the corresponding elements in `lista_A`, and `pref` is the sum of the elements in `lista_A` that were less than the corresponding elements in `lista_B` plus the accumulated `soma_b` values from previous iterations.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: After the loop executes all the iterations, `n` is greater than `k`, `i` is `n - 1`, `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 200,000, `lista_B` is a list of integers of length `n` where 1 ≤ b_i ≤ 10^9, and `lista_B` is in its original order, `lista_A` is a list of integers provided by the user input and has been reversed, `soma_b` is the sum of the last `n - k - 1` elements of `lista_B` that were not less than the corresponding elements in `lista_A` plus the sum of the elements in `lista_B` from index `n - k` to `n - 1`, `pref` is the sum of the elements in `lista_A` that were less than the corresponding elements in `lista_B` plus the accumulated `soma_b` values from previous iterations, `resultado` is the minimum value between the initial `resultado` (which was infinity) and the values of `pref + soma_b + lista_A[i]` for each iteration from `i = n - k` to `i = n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for i from n - k to n - 1)
#Overall this is what the function does:The function reads two integers `n` and `k` from user input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It reverses both lists. The function then calculates a value `resultado` which is the minimum of a series of sums involving elements from `lista_A` and `lista_B`, specifically focusing on the last `k` elements of the lists. The final value of `resultado` is printed. The function does not return any value; it only prints the result.

#State of the program right berfore the function call: numero_testes is a positive integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` must be greater than or equal to the number of iterations, `func_1()` has been called `numero_testes` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters and does not return any value. It reads an integer `numero_testes` from the user input, which must be a positive integer between 1 and 10^4. The function then calls `func_1` exactly `numero_testes` times. After the function concludes, `numero_testes` remains unchanged, and `func_1` has been executed the specified number of times. The primary purpose of `func_2` is to repeatedly execute `func_1` a user-specified number of times.

