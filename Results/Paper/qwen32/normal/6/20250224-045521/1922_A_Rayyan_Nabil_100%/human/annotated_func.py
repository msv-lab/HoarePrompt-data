#State of the program right berfore the function call: n is a positive integer representing the length of the strings a, b, and c, and a, b, c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop has finished executing all iterations without returning 'YES'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` checks if there exists at least one position in the strings `a`, `b`, and `c` (each of length `n`) where the characters in `a` and `b` are different from the character in `c`. If such a position is found, it returns 'YES'. If no such position exists after checking all positions, it returns 'NO'.

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
        
    #State: `n` is the input integer from the last iteration, `a` is the string of exactly `n` lowercase Latin letters from the last iteration, `b` is the string of exactly `n` lowercase Latin letters from the last iteration, `c` is the string of exactly `n` lowercase Latin letters from the last iteration, `t` is the input integer greater than 0, and `results` is a list containing `t` elements, each of which is the return value of `func_1(n, a, b, c)` for each iteration.
    for result in results:
        print(result)
        
    #State: `n` is the input integer from the last iteration, `a` is the string of exactly `n` lowercase Latin letters from the last iteration, `b` is the string of exactly `n` lowercase Latin letters from the last iteration, `c` is the string of exactly `n` lowercase Latin letters from the last iteration, `t` is the input integer greater than 0, and `results` is a list containing `t` elements, each of which is the return value of `func_1(n, a, b, c)` for each iteration. The loop has finished executing all `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is a positive integer between 1 and 20. It then processes these strings and prints "increasing" if `a` is lexicographically smaller than `b` and `b` is lexicographically smaller than `c`, "decreasing" if `a` is lexicographically larger than `b` and `b` is lexicographically larger than `c`, and "neither" in all other cases.

