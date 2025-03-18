#State of the program right berfore the function call: n is a positive integer representing the number of people in the queue besides Kirill, and k is a positive integer such that 1 <= k <= n, representing the maximum allowable final position of Kirill. lista_A is a list of n integers where each element a_i represents the cost Kirill has to pay to swap places with the i-th person. lista_B is a list of n integers where each element b_i represents the additional cost Kirill has to pay to each person between the i-th and j-th positions during a swap.
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
        
    #State: `pref` is the cumulative sum of selected elements from `lista_A` and accumulated `soma_b` values, and `soma_b` is the sum of the remaining elements from `lista_B`.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for `i` in the range `[n - k, n - 1]`, and `soma_b` is the sum of `soma_b` and `lista_B[i]` for `i` in the range `[n - k, n - 1]`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for i in the range [n - k, n - 1])
#Overall this is what the function does:The function calculates and returns the minimum total cost for Kirill to move to a position no more than `k` from the front of the queue, given the costs of individual swaps (`lista_A`) and the additional costs for each person between the swapped positions (`lista_B`).

#State of the program right berfore the function call: numero_testes is an integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is an integer input by the user such that 1 <= `numero_testes` <= 10^4. The function `func_1()` has been executed `numero_testes` times.
#Overall this is what the function does:The function `func_2` reads an integer `numero_testes` from the user input, which represents the number of tests to be performed. It then executes the function `func_1` exactly `numero_testes` times. The function `func_2` does not accept any parameters and does not return any value.

