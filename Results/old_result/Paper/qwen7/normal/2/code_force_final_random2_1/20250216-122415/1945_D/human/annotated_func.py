#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 200,000; lista_A is a list of n integers where each integer is between 1 and 10^9 inclusive; lista_B is a list of n integers where each integer is between 1 and 10^9 inclusive.
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
        
    #State: After the loop executes all iterations, `i` will be `n - k - 1`, `n - k` will be 0 (since `i` reaches the end of the range), `soma_b` will be the sum of all elements in `lista_B`, and `pref` will be updated based on the conditions inside the loop.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `i` is `n - k`, `n - k` is 0, `soma_b` is the sum of all elements in `lista_B` from index 0 to `n - k`, and `resultado` is assigned the minimum value between its current value and `(pref + soma_b + lista_A[i])` for every `i` in the range `[n - k, n)`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value between its current value and (pref + soma_b + lista_A[0]))
#Overall this is what the function does:The function accepts two positive integers n and k, along with two lists of integers lista_A and lista_B, each containing n integers. It calculates and returns the minimum possible sum based on specific conditions involving elements from these lists. Specifically, it compares elements from lista_A and lista_B, updates a running sum, and finds the minimum sum that can be achieved under the given constraints.

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, and a list of n integers b_1, b_2, ..., b_n where 1 ≤ b_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `func_1()` has been called `numero_testes` times.
    #
    #Explanation: Since the loop runs `numero_testes` times and `func_1()` is called in each iteration, after all iterations of the loop have finished, `func_1()` will have been called exactly `numero_testes` times. The value of `numero_testes` must be greater than 0 for the loop to execute at least once, as stated in the given conditions. Therefore, after all iterations, `func_1()` will have been called `numero_testes` times.
#Overall this is what the function does:The function processes multiple test cases, each involving integers n and m, and two lists of n integers a and b. It ensures that 1 ≤ m ≤ n ≤ 200,000 and 1 ≤ a_i, b_i ≤ 10^9 for each test case. After processing all test cases, the function calls `func_1()` exactly `numero_testes` times, where `numero_testes` is an integer between 1 and 10^4. The function does not return any value.

