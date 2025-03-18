#State of the program right berfore the function call: n is a positive integer representing the number of people in the queue besides Kirill, and k is a positive integer such that 1 <= k <= n. lista_A is a list of n integers where each element a_i represents the cost Kirill has to pay to bribe the i-th person. lista_B is a list of n integers where each element b_i represents the cost Kirill has to pay to each person between the j-th and i-th person when bribing the j-th person to position i.
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
        
    #State: - `n` and `k` remain unchanged.
    #- `lista_A` and `lista_B` remain unchanged.
    #- `soma_b` will be the sum of elements in `lista_B` from indices `0` to `n-k-1` where `lista_A[i] >= lista_B[i]`.
    #- `pref` will be the accumulated sum based on the conditions described above.
    #
    #Output State:
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `n` and `k` remain unchanged; `lista_A` and `lista_B` remain unchanged; `soma_b` is the sum of elements in `lista_B` from indices `0` to `n-1` where `lista_A[i] >= lista_B[i]` for `i` from `0` to `n-k-1`, plus the sum of elements in `lista_B` from indices `n-k` to `n-1`; `pref` remains unchanged; `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for `i` from `n-k` to `n-1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for i from n-k to n-1)
#Overall this is what the function does:The function calculates and returns the minimum total cost Kirill has to pay to bribe his way to the k-th position in a queue, given the costs to bribe individuals and the additional costs to bribe through others.

#State of the program right berfore the function call: This function does not take any parameters. It is designed to read the number of test cases from the input and then call another function `func_1()` for each test case.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` remains unchanged, and `func_1()` has been executed `numero_testes` times.
#Overall this is what the function does:The function `func_2` reads the number of test cases from the input and executes the function `func_1` for each test case.

