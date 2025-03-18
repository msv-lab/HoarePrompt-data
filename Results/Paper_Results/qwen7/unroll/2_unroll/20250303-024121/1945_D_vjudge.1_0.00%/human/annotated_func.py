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
        
    #State: Output State: `soma_b` is 0, `n` is the same input integer, `k` is the same input integer, `pref` is the sum of elements in `lista_B` from index `n-k` to `n-1` that are greater than or equal to the corresponding elements in `lista_A`, and `lista_B` is a list of `n` integers in reverse order where each integer is between 1 and 10^9 inclusive.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `soma_b` is the sum of elements in `lista_B` from index `n-k` to `n-1`, `n` is the same input integer, `k` is the same input integer, `pref` is the sum of elements in `lista_B` from index `n-k` to `n-1` that are greater than or equal to the corresponding elements in `lista_A`, `resultado` is the minimum value obtained by adding `pref` and `soma_b` for each iteration, and `lista_B` is a list of `n` integers in reverse order where each integer is between 1 and 10^9 inclusive.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value obtained by adding pref and soma_b for each iteration)
#Overall this is what the function does:The function accepts two lists, `lista_A` and `lista_B`, both containing `n` integers where each integer is between 1 and 10^9 inclusive, and two positive integers `n` and `k` such that 1 ≤ k ≤ n ≤ 200,000. It calculates and returns the minimum value obtained by adding the sum of elements in `lista_B` from index `n-k` to `n-1` (if these elements are greater than or equal to the corresponding elements in `lista_A`) to the sum of remaining elements in `lista_A` from index `n-k` to `n-1`.

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, and the lists a and b contain n integers each, where 1 ≤ a_i, b_i ≤ 10^9.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `numero_testes` is an integer such that 1 ≤ `numero_testes` ≤ 10^4, and it is decremented by 1 after each iteration of the loop until it reaches 0.
#Overall this is what the function does:The function processes a series of test cases defined by `numero_testes`, `n`, `m`, `a`, and `b`. It iterates through `numero_testes` test cases, where for each test case, it takes two integers `n` and `m` and two lists `a` and `b` of length `n`. After processing all test cases, it outputs the results based on the given inputs.

