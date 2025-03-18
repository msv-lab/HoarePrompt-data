#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The function does not return 'YES' if for all indices `i` from 0 to `n-1`, either `a[i] == c[i]` or `b[i] == c[i]`.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts three strings `a`, `b`, and `c`, each consisting of exactly `n` lowercase Latin letters, where `n` is a positive integer between 1 and 20 inclusive. The function checks each position in the strings to determine if the character in `c` at that position matches the character in either `a` or `b`. If there is at least one position where the character in `c` does not match the character in either `a` or `b`, the function returns 'YES'. Otherwise, it returns 'NO'.

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
        
    #State: `n` is the integer value of the last user input, `a` is the last string of exactly `n` lowercase Latin letters provided by the user input, `b` is the last string of exactly `n` lowercase Latin letters provided by the user input, `c` is the last string of exactly `n` lowercase Latin letters provided by the user input, `t` is 0, `results` is a list containing `t` elements which are the results of `func_1(n, a, b, c)` called `t` times.
    for result in results:
        print(result)
        
    #State: `n` is the integer value of the last user input, `a` is the last string of exactly `n` lowercase Latin letters provided by the user input, `b` is the last string of exactly `n` lowercase Latin letters provided by the user input, `c` is the last string of exactly `n` lowercase Latin letters provided by the user input, `t` is 1, `results` is a list containing 1 element which is the result of `func_1(n, a, b, c)`
#Overall this is what the function does:The function reads an integer `t` from the user, representing the number of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each of length `n` (where `n` is a positive integer between 1 and 20 inclusive). It then processes these strings using `func_1` and prints the result for each test case.

