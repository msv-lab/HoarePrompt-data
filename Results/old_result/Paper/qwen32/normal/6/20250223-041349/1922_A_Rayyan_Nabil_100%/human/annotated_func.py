#State of the program right berfore the function call: n is a positive integer representing the length of strings a, b, and c, and a, b, and c are strings of lowercase Latin letters each of length n.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop has completed all `n` iterations without returning 'YES'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts three strings `a`, `b`, and `c`, each of length `n`, where `n` is a positive integer. It checks each corresponding character in the strings `a` and `b` against the character in `c`. If there is at least one position where both `a` and `b` have characters different from the character in `c`, the function returns 'YES'. If no such position exists after checking all characters, it returns 'NO'.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and a, b, c are strings each consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: `n` is the input integer such that 1 <= `n` <= 20; `a` is the newly input string consisting of exactly `n` lowercase Latin letters; `b` is the newly input string consisting of exactly `n` lowercase Latin letters; `c` is the newly input string consisting of exactly `n` lowercase Latin letters; `t` is an integer such that `t` >= 0; `results` is a list containing `t` elements, all of which are the return value of `func_1(n, a, b, c)` for each iteration.
    for result in results:
        print(result)
        
    #State: `n` is the input integer such that 1 <= `n` <= 20; `a` is the newly input string consisting of exactly `n` lowercase Latin letters; `b` is the newly input string consisting of exactly `n` lowercase Latin letters; `c` is the newly input string consisting of exactly `n` lowercase Latin letters; `t` is an integer such that `t` >= 0; `results` is a list containing `t` elements, all of which are the return value of `func_1(n, a, b, c)` for each iteration.
#Overall this is what the function does:The function `func_2` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters. It then processes these strings using the function `func_1` and collects the results. Finally, it prints the results for each test case.

