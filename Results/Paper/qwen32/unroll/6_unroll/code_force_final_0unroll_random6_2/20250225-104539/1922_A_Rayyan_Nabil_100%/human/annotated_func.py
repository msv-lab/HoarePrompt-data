#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: the function returns 'NO'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is a positive integer between 1 and 20. It checks if there is any position `i` where neither `a[i]` nor `b[i]` matches `c[i]`. If such a position is found, it returns 'YES'. If no such position exists, it returns 'NO'.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `n` is the integer value from the last iteration, `a`, `b`, and `c` are the strings from the last iteration, and `results` is a list containing the results of `func_1` for each of the `t` iterations.
    for result in results:
        print(result)
        
    #State: `n` is the integer value from the last iteration, `a`, `b`, and `c` are the strings from the last iteration, and `results` is a list containing the results of `func_1` for each of the `t` iterations.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is a positive integer such that 1 <= n <= 20. It then processes these strings using another function `func_1` and stores the results. After processing all test cases, it prints the results for each one.

