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
        
    #State: Output State: `soma_b` is 0, `n` is an integer, `k` is an integer, `lista_A` is a list of n integers, `lista_B` is a list of integers, `pref` is the sum of elements in `lista_A` up to index `i` where `lista_A[i] < lista_B[i]` for each iteration from 0 to `n-k-1`, and `pref` is also incremented by `soma_b` whenever the condition is met.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: Output State: `soma_b` is the sum of elements in `lista_B` from index `n-k` to `n-1`, `n` is an integer, `k` is an integer, `lista_A` is a list of n integers, `lista_B` is a list of integers, `pref` is the sum of elements in `lista_A` up to index `i` where `lista_A[i] < lista_B[i]` for each iteration from 0 to `n-k-1`, and `resultado` is the minimum value among `pref + soma_b + lista_A[i]` for all `i` in the range `n-k` to `n-1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value among pref + soma_b + lista_A[i] for all i in the range n-k to n-1)
#Overall this is what the function does:The function accepts two positive integers n and k, along with two lists of integers lista_A and lista_B, each containing n integers. It calculates and returns the minimum value of the expression `pref + soma_b + lista_A[i]` for all indices i in the range from `n-k` to `n-1`. Here, `pref` is the sum of elements in lista_A up to index i where lista_A[i] < lista_B[i], and `soma_b` is the sum of elements in lista_B from index `n-k` to i.

#State of the program right berfore the function call: numero_testes is an integer such that 1 ≤ numero_testes ≤ 10^4. For each test case, n and m are integers such that 1 ≤ m ≤ n ≤ 200,000, and the subsequent lines contain n integers a_1, a_2, ..., a_n and n integers b_1, b_2, ..., b_n, where 1 ≤ a_i, b_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: Output State: `func_1()` has been executed `numero_testes` times.
#Overall this is what the function does:The function processes multiple test cases by executing `func_1()` for each test case specified by the user. After processing all test cases, it outputs the results of `func_1()` for each case.

