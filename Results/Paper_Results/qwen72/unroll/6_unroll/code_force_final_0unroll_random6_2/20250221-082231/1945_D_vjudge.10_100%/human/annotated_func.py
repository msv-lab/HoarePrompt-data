#State of the program right berfore the function call: pergunta is an integer representing the number of test cases (1 <= pergunta <= 10^4), a and b are lists of integers of length n (1 <= a_i, b_i <= 10^9), and n and m are integers such that 1 <= m <= n <= 200,000. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func_1(pergunta, a, b, n, m):
    x = 0
    for i in range(n - 1, -1, -1):
        if i < m:
            pergunta = min(pergunta, x + a[i])
        
        x += min(a[i], b[i])
        
    #State: pergunta is the minimum value between the initial pergunta and the sum of the minimum values of a[i] and x for the first m elements of the list a, starting from the end. x is the sum of the minimum values of a[i] and b[i] for all elements from the end of the list to the beginning. The values of a, b, n, and m remain unchanged.
    print(pergunta)
    #This is printed: pergunta (where pergunta is the minimum value between the initial pergunta and the sum of the minimum values of a[i] and x for the first m elements of the list a, starting from the end, and x is the sum of the minimum values of a[i] and b[i] for all elements from the end of the list to the beginning)
#Overall this is what the function does:The function `func_1` accepts an integer `pergunta` representing the number of test cases, two lists of integers `a` and `b` of length `n`, and two integers `n` and `m` with constraints 1 <= m <= n <= 200,000. It processes the lists `a` and `b` and updates `pergunta` to the minimum value between the initial `pergunta` and the sum of the minimum values of `a[i]` and `x` for the first `m` elements of the list `a`, starting from the end. Here, `x` is the cumulative sum of the minimum values of `a[i]` and `b[i]` for all elements from the end of the list to the beginning. The function then prints the final value of `pergunta`. The values of `a`, `b`, `n`, and `m` remain unchanged.

