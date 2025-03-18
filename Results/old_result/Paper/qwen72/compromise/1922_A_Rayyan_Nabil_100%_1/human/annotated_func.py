#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop will either return 'YES' if there is at least one index i where both a[i] and b[i] are different from c[i], or it will not return anything (i.e., the function will continue executing or terminate based on the context outside the loop) if no such index exists. The values of n, a, b, and c remain unchanged.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and three strings `a`, `b`, and `c` of length `n` consisting of lowercase Latin letters. It checks if there is any index `i` where both `a[i]` and `b[i]` are different from `c[i]`. If such an index is found, the function returns 'YES'. If no such index exists, the function returns 'NO'. The values of `n`, `a`, `b`, and `c` remain unchanged.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 20, a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: `t` is the same input integer such that 1 <= t <= 1000, `n` is the last input integer such that 1 <= n <= 20, `a`, `b`, and `c` are the last input strings consisting of exactly `n` lowercase Latin letters, `results` is a list containing `t` elements, where each element is the result of calling `func_1(n, a, b, c)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: The `results` list remains unchanged, and `t`, `n`, `a`, `b`, and `c` retain their initial values. The loop prints each element in the `results` list, one per line.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 1000`. It then performs `t` iterations, each time reading an integer `n` (where `1 <= n <= 20`) and three strings `a`, `b`, and `c` (each consisting of exactly `n` lowercase Latin letters). For each iteration, it calls `func_1(n, a, b, c)` and appends the result to a list `results`. After all iterations, it prints each element in the `results` list, one per line. The function does not return any value; it only prints the results.

