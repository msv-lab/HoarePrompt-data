#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 200,000. lista_A and lista_B are lists of integers of length n, where each element is in the range 1 ≤ a_i, b_i ≤ 10^9.
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
        
    #State: After all iterations of the loop, `i` is `n - k - 1`, `soma_b` is the sum of the last `k` elements of `lista_B` that were not compared with smaller elements in `lista_A`, and `pref` is the sum of the elements in `lista_A` that were less than their corresponding elements in `lista_B` plus the cumulative sum of `soma_b` at those points. The lists `lista_A` and `lista_B` remain unchanged.
    resultado = float('inf')
    for i in range(n - k, n):
        resultado = min(resultado, pref + soma_b + lista_A[i])
        
        soma_b += lista_B[i]
        
    #State: After all iterations of the loop, `i` is `n - 1`, `n` must be greater than or equal to `k`, `soma_b` is the sum of the last `k` elements of `lista_B` that were not compared with smaller elements in `lista_A` plus the sum of the last `k` elements of `lista_B`, `pref` is the sum of the elements in `lista_A` that were less than their corresponding elements in `lista_B` plus the cumulative sum of `soma_b` at those points, `lista_A` and `lista_B` remain unchanged, `resultado` is the minimum value of `pref + soma_b + lista_A[i]` for all `i` from `n - k` to `n - 1`.
    print(resultado)
    #This is printed: resultado (where resultado is the minimum value of pref + soma_b + lista_A[i] for all i from n - k to n - 1)
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, followed by two lists of integers `lista_A` and `lista_B` of length `n`. It reverses both lists and then computes a value `resultado` which is the minimum of a specific calculation involving elements from `lista_A` and `lista_B`. The final value of `resultado` is printed. The lists `lista_A` and `lista_B` are reversed but otherwise remain unchanged. The function does not return any value; it only prints the result.

#State of the program right berfore the function call: numero_testes is a positive integer such that 1 <= numero_testes <= 10^4.
def func_2():
    numero_testes = int(input())
    for _ in range(numero_testes):
        func_1()
        
    #State: `numero_testes` is a positive integer between 1 and 10^4, and `func_1()` has been called `numero_testes` times.
#Overall this is what the function does:The function `func_2` reads an integer `numero_testes` from user input, ensuring it is a positive integer between 1 and 10^4. It then calls the function `func_1` exactly `numero_testes` times. The function does not accept any parameters and does not return any value. After the function concludes, `numero_testes` remains a positive integer between 1 and 10^4, and `func_1` has been executed `numero_testes` times.

