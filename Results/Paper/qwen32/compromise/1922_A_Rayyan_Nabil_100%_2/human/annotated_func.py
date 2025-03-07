#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: n is a positive integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function checks if there is at least one position in the strings `a`, `b`, and `c` where both `a` and `b` differ from `c`. If such a position exists, it returns 'YES'; otherwise, it returns 'NO'.

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
        
    #State: `n` is the number of characters in the last set of strings `a`, `b`, and `c`, which are the strings from the last iteration. `a`, `b`, and `c` are the strings from the last iteration. `t` is unchanged. `results` is a list containing the results from each of the `t` iterations.
    for result in results:
        print(result)
        
    #State: n is the number of characters in the last set of strings a, b, and c, which are the strings from the last iteration. a, b, and c are the strings from the last iteration. t is unchanged. results is a list containing the results from each of the t iterations. The elements of results have been printed.
#Overall this is what the function does:The function `func_2` reads an integer `t` representing the number of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each of length `n` (where `1 <= n <= 20`). It then computes and prints the number of positions at which the corresponding characters in the strings `a`, `b`, and `c` are all the same.

