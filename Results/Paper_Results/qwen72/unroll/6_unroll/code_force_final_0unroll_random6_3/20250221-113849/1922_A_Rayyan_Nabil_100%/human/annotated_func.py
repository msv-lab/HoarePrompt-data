#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop will either return 'YES' if there is at least one index i where both a[i] and b[i] are different from c[i], or it will complete all iterations without returning if no such index exists. In the latter case, the state of n, a, b, and c remains unchanged.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. It checks if there is at least one index `i` where both `a[i]` and `b[i]` are different from `c[i]`. If such an index is found, the function returns 'YES'. If no such index exists, the function returns 'NO'. The function does not modify the input parameters.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, n is a positive integer such that 1 <= n <= 20, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `n` is the last input integer such that 1 <= n <= 20, `a`, `b`, and `c` are the last input strings of length `n` consisting of lowercase Latin letters, `results` is a list containing `t` elements, each element is the result of the function `func_1(n, a, b, c)` for each iteration.
    for result in results:
        print(result)
        
    #State: The list `results` remains unchanged, and all elements of `results` have been printed to the console. The variables `t`, `n`, `a`, `b`, and `c` retain their initial values.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 1000`. It then iterates `t` times, each time reading an integer `n` and three strings `a`, `b`, and `c`, where `1 <= n <= 20` and each string is of length `n` consisting of lowercase Latin letters. For each iteration, it calls `func_1` with the parameters `n`, `a`, `b`, and `c`, and appends the result to a list `results`. After all iterations, it prints each element in `results` to the console. The function does not return any value. After the function concludes, the list `results` contains `t` elements, each being the result of `func_1` for the corresponding iteration, and all elements of `results` have been printed to the console. The variables `t`, `n`, `a`, `b`, and `c` retain their final values from the last iteration.

