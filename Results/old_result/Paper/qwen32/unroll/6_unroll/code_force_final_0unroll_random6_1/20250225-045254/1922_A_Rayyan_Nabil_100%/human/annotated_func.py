#State of the program right berfore the function call: n is a positive integer representing the length of the strings a, b, and c, and a, b, and c are strings of length n consisting of lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: the function returns None.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts three strings `a`, `b`, and `c`, each of length `n` where `n` is a positive integer, and consisting of lowercase Latin letters. It checks if there is any position `i` where both `a[i]` and `b[i]` are different from `c[i]`. If such a position exists, it returns 'YES'. If no such position exists after checking all positions, it returns 'NO'.

#State of the program right berfore the function call: n is a positive integer (1 <= n <= 20), a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: n is the integer value read in the last iteration, a is the string read in the last iteration, b is the string read in the last iteration, c is the string read in the last iteration, t is the same as the initial value, results is a list of results from each func_1 call.
    for result in results:
        print(result)
        
    #State: n is the integer value read in the last iteration, a is the string read in the last iteration, b is the string read in the last iteration, c is the string read in the last iteration, t is the same as the initial value, results is a list of results from each func_1 call.
#Overall this is what the function does:The function `func_2` reads an integer `t` representing the number of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is a positive integer between 1 and 20 inclusive. It processes these strings using the function `func_1` and collects the results. Finally, it prints the result for each test case.

