#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 200,000, lista_A is a list of n integers where 1 ≤ a_i ≤ 10^9, and lista_B is a list of n integers where 1 ≤ b_i ≤ 10^9.
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
        
    #State: Output State: After the loop executes all the iterations, the value of `i` will be `n - k - 1`, `pref` will be the sum of all `lista_A[i]` where `lista_A[i] < lista_B[i]` plus the cumulative sum of `lista_B[i]` where `lista_A[i] >= lista_B[i]` from `i=0` to `i=n-k-1`, and `soma_b` will be 0 if there was no `lista_A[i]` that was greater than or equal to `lista_B[i]` from `i=0` to `i=n-k-1`.
    #
    #This means that `pref` accumulates the values from `lista_A` when the corresponding elements in `lista_A` are smaller than those in `lista_B`, and also adds the cumulative sum of `lista_B` when `lista_A` elements are not smaller. `soma_b` remains 0 because it gets reset to 0 whenever a condition is met in the if statement.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `i` is `n - 1`; `soma_b` is the sum of `lista_B` from index `n - k` to `n - 1`; `pref` is the cumulative sum of `lista_A` from index `n - k` to `n - 2`; `resultado` is the minimum value obtained from the expression `pref + soma_b + lista_A[i]` for each iteration of the loop.
    #
    #In this final state, the loop has executed for all iterations from `i = n - k` to `i = n - 1`. The variable `i` has reached its maximum value of `n - 1`. The variable `soma_b` contains the sum of all elements in `lista_B` from the start of the loop until the last iteration. The variable `pref` holds the cumulative sum of `lista_A` from the start of the loop until the second-to-last iteration. The variable `resultado` retains the minimum value calculated during any iteration of the loop using the formula `pref + soma_b + lista_A[i]`.
    print(resultado)
    #This is printed: resultado (the minimum value obtained from the expression pref + soma_b + lista_A[i] for each iteration of the loop)
#Overall this is what the function does:The function accepts two lists, `lista_A` and `lista_B`, both containing `n` integers within the range 1 to \(10^9\), and two positive integers `n` and `k` where \(1 \leq k \leq n \leq 200,000\). It processes these inputs by comparing elements of `lista_A` and `lista_B` up to index `n-k-1`, accumulating certain sums based on comparison results, and then calculates a minimum value involving these sums and the remaining elements of `lista_A`. Finally, it prints this minimum value.

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, a is a list of n integers where 1 ≤ a_i ≤ 10^9, and b is a list of n integers where 1 ≤ b_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 × 10^5.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `func_1()` has been called `numero_testes` times.
    #
    #Explanation: Since the loop runs `numero_testes` times and `func_1()` is called in each iteration, after all iterations of the loop have finished, `func_1()` will have been called exactly `numero_testes` times. The value of `numero_testes` remains within the range \(1 \leq \text{numero_testes} \leq 10^4\) as no operations inside or outside the loop change its value.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads `numero_testes`, `n`, `m`, list `a`, and list `b`. It then calls `func_1()` exactly `numero_testes` times, performing unspecified operations defined in `func_1()`. After processing all test cases, it does not return any value but ensures that `func_1()` has been called the required number of times.

