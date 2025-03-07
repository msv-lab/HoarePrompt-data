#State of the program right berfore the function call: n is an integer representing the number of people in the queue besides Kirill, and k is an integer representing the maximum allowable final position of Kirill such that 1 <= k <= n. lista_A is a list of n integers where each element represents the cost a_i for Kirill to swap positions with the i-th person. lista_B is a list of n integers where each element represents the cost b_i for Kirill to pass the i-th person during a swap. Both lista_A and lista_B contain positive integers.
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
        
    #State: `n` is the first integer read from the input, `k` is the second integer read from the input, `lista_A` is the reversed list of integers read from the input, `lista_B` is the reversed version of the newly read list of integers from the input, `soma_b` is the sum of elements in `lista_B` from index `n-k` to the end of the list, `pref` is the accumulated sum based on the loop's conditions.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: `resultado` is the minimum value of `pref + soma_b + lista_A[i]` encountered during the loop, `soma_b` is the sum of elements in `lista_B` from index `n-k` to `n-1`, `i` is `n`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] encountered during the loop, with i ranging from some starting point to n)
#Overall this is what the function does:The function calculates and prints the minimum total cost for Kirill to reach a position no greater than `k` in a queue, given the costs of swapping positions (`lista_A`) and passing people during swaps (`lista_B`).

#State of the program right berfore the function call: This function does not take any parameters. It reads the number of test cases from the input and iterates through each test case by calling `func_1()`.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is an integer read from the input and must be greater than 0; `func_1()` was called `numero_testes` times.
#Overall this is what the function does:The function `func_2` reads an integer from the input representing the number of test cases and then calls `func_1()` for each of those test cases.

