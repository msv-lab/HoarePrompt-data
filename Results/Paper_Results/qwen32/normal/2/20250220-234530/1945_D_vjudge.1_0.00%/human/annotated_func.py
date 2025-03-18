#State of the program right berfore the function call: n is an integer representing the number of people in the queue besides Kirill, and k is an integer representing the maximum allowable final position of Kirill such that 1 <= k <= n. lista_A is a list of n integers where each element a_i represents the cost Kirill has to pay to swap places with the i-th person. lista_B is a list of n integers where each element b_i represents the cost Kirill has to pay to the person at position k for each k such that j < k < i when swapping positions with the j-th person.
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
        
    #State: `pref` is the accumulated sum of relevant elements from `lista_A` and `soma_b` is the accumulated sum of relevant elements from `lista_B` after all iterations.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `pref` remains unchanged, `soma_b` is the sum of `lista_B[n - k]` to `lista_B[n - 1]`, and `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for `i` from `n - k` to `n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for i from n - k to n - 1)
#Overall this is what the function does:The function calculates and prints the minimum total cost Kirill has to pay to move to a position no later than `k` in the queue, considering the direct swap costs specified in `lista_A` and the indirect swap costs specified in `lista_B`.

#State of the program right berfore the function call: This function does not take any parameters. It reads an integer from the input which represents the number of test cases (numero_testes). This integer is expected to be between 1 and 10^4 inclusive.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: numero_testes is 0.
#Overall this is what the function does:The function `func_2` reads an integer from the input representing the number of test cases and processes each test case by calling `func_1` for each one.

