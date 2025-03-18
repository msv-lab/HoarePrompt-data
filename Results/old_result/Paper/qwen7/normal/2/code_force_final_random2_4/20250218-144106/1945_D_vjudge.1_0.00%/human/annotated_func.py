#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 200,000, lista_A is a list of n integers where each integer is between 1 and 10^9 inclusive, and lista_B is a list of n integers where each integer is between 1 and 10^9 inclusive.
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
        
    #State: Output State: `soma_b` is an integer, `n` is greater than or equal to `k + 1`, `k` is an integer, `lista_A` is a list of `n` integers in reverse order, `lista_B` is a list of integers in reverse order, `pref` is either `soma_b + lista_A[i]` if `lista_A[i] < lista_B[i]` or `0` if `lista_A[i] >= lista_B[i]` for all `i` where `0 <= i < n`, `i` is `n - k - 1`. If `lista_A[i] < lista_B[i]`, `soma_b` remains unchanged and `pref` is set to `soma_b + lista_A[i]`. Otherwise, `soma_b` is increased by `lista_B[i]` and `pref` remains unchanged.
    #
    #In simpler terms, after the loop has executed all its iterations, `soma_b` will hold the sum of `lista_A[i]` for all `i` where `lista_A[i] < lista_B[i]` and `i` ranges from `0` to `n - k - 1`. The variable `pref` will be the cumulative sum of `soma_b + lista_A[i]` whenever `lista_A[i] < lista_B[i]`, otherwise, it will be `0` for those cases. The loop iterates from `i = 0` to `i = n - k - 1`, so the final value of `i` will be `n - k - 1`. The lists `lista_A` and `lista_B` remain in their reversed states as they are not modified within the loop.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `soma_b` is the sum of all elements in `lista_B` from index `n - k` to the end of the list, `n` remains the same, `k` remains the same, `lista_A` remains the same, `lista_B` remains the same, `pref` remains the same, `i` is the last value it was set to within the range `[n - k, n)`, `resultado` is the minimum value it was updated to during the loop, which is the minimum of `resultado` and `pref + soma_b + lista_A[i]` for all iterations of the loop.
    #
    #In simpler terms, after the loop completes all its iterations, `soma_b` will be the sum of all elements in `lista_B` starting from index `n - k` to the end of the list. The variable `resultado` will hold the smallest value it was updated to during any iteration of the loop, considering the expression `pref + soma_b + lista_A[i]`. All other variables (`n`, `k`, `lista_A`, `lista_B`, `pref`, and `i`) will retain their final values from the last iteration of the loop.
    print(resultado)
    #This is printed: the minimum value of pref + soma_b + lista_A[i] for all iterations of the loop
#Overall this is what the function does:The function accepts two positive integers `n` and `k` (with the condition 1 ≤ k ≤ n ≤ 200,000), and two lists `lista_A` and `lista_B` each containing `n` integers ranging from 1 to 10^9. It processes these inputs by comparing elements of `lista_A` and `lista_B` in reverse order, calculating a cumulative sum (`soma_b`) of elements in `lista_B` and determining a prefix sum (`pref`) based on certain conditions. Finally, it computes the minimum value of `pref + soma_b + lista_A[i]` for specific indices and prints this minimum value.

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, and the lists a and b are lists of n integers where 1 ≤ a_i, b_i ≤ 10^9 for all 1 ≤ i ≤ n.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `numero_testes` is an integer such that \(1 \leq \text{numero_testes} \leq 10^3\) and \(\text{numero_testes} > 2\); `func_1()` has been called `numero_testes` times.
    #
    #This means that after all the iterations of the loop have finished, `numero_testes` will be an integer between 1 and 1000 (inclusive), but it will definitely be greater than 2, as the loop runs from 1 to `numero_testes - 1`. Additionally, `func_1()` will have been called exactly `numero_testes` times.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \(n\) and \(m\), and two lists \(a\) and \(b\). It then calls `func_1()` exactly `numero_testes` times, where `numero_testes` is initially read from input and must be between 1 and 10,000 inclusive. After processing all test cases, `numero_testes` is guaranteed to be between 1 and 1,000 inclusive, but it will always be greater than 2. The function does not return any value.

