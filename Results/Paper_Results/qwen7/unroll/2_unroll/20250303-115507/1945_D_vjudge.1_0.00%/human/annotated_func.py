#State of the program right berfore the function call: n and k are integers such that 1 ≤ m ≤ k ≤ n ≤ 200,000, lista_A is a list of n integers where 1 ≤ a_i ≤ 10^9, and lista_B is a list of n integers where 1 ≤ b_i ≤ 10^9.
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
        
    #State: Output State: `soma_b` is 0, `n` is an integer, `k` is an integer, `lista_A` is a list of integers, `lista_B` is a list of integers, `pref` is the sum of `pref` plus `soma_b` for each index `i` where `i` is less than `n - k` and `lista_A[i]` is less than `lista_B[i]`, plus `lista_A[i]`, and `soma_b` is the sum of `soma_b` and `lista_B[i]` for each index `i` where `i` is less than `n - k` and `lista_A[i]` is greater than or equal to `lista_B[i]`.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `soma_b` is the sum of `soma_b` and `lista_B[i]` for each index `i` from `n - k` to `n-1`, `pref` remains the same as its initial value, `resultado` is the minimum value between `resultado` and `pref + soma_b + lista_A[i]` for each index `i` from `n - k` to `n-1`, and `soma_b` is the sum of `soma_b` and `lista_B[i]` for each index `i` from `n - k` to `n-1`.
    print(resultado)
    #This is printed: resultado (the minimum value between resultado and pref + soma_b + lista_A[i] for each index i from n - k to n-1)
#Overall this is what the function does:The function accepts two integers \( n \) and \( k \), and two lists \( \text{lista\_A} \) and \( \text{lista\_B} \). It calculates and returns the minimum value of \( \text{pref} + \text{soma\_b} + \text{lista\_A}[i] \) for each index \( i \) from \( n - k \) to \( n-1 \), where \( \text{pref} \) is the sum of elements in \( \text{lista\_A} \) that are less than corresponding elements in \( \text{lista\_B} \) up to index \( n - k \), and \( \text{soma\_b} \) is the cumulative sum of elements in \( \text{lista\_B} \) from index \( 0 \) to \( n - k - 1 \).

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, a is a list of n integers where 1 ≤ a_i ≤ 10^9, and b is a list of n integers where 1 ≤ b_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 × 10^5.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `func_1()` has been executed `numero_testes` times.
#Overall this is what the function does:The function processes multiple test cases, executing `func_1()` for each one. It reads the number of test cases (`numero_testes`) from input, then for each test case, it calls `func_1()`. After processing all test cases, it outputs the results of `func_1()` for each test case.

