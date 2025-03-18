#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_1(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: Output State: The value returned by the function is either 'YES' or None (if the loop completes without encountering any condition where `a[i] != c[i]` and `b[i] != c[i]` for any `i`).
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts three parameters: an integer \( n \) (where \( 1 \leq n \leq 20 \)), and two strings \( a \) and \( b \) each consisting of exactly \( n \) lowercase Latin letters, along with a third string \( c \) also consisting of exactly \( n \) lowercase Latin letters. The function checks if for every index \( i \) from 0 to \( n-1 \), either \( a[i] \) or \( b[i] \) is equal to \( c[i] \). If such an index is found where both \( a[i] \neq c[i] \) and \( b[i] \neq c[i] \), the function returns 'YES'. If no such index exists, the function returns 'NO'. The final state of the program after the function concludes is that it returns either 'YES' or 'NO'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 20, a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_2():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: `results` is a list containing `t` elements, where each element is the return value of `func_1(n, a, b, c)` for the corresponding iteration. `t` is an input integer between 1 and 1000, and for each iteration, `n` is an integer between 1 and 20, while `a`, `b`, and `c` are strings consisting of exactly `n` lowercase Latin letters.
    for result in results:
        print(result)
        
    #State: The output state will be the same as the initial state because the loop simply iterates over the `results` list and prints each element. The `results` list remains unchanged after the loop executes all the iterations.
#Overall this is what the function does:The function reads multiple sets of inputs, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (length of strings), and three strings \( a \), \( b \), and \( c \) (each of length \( n \)). For each set of inputs, it calls another function `func_1` to process the strings and stores the result. After processing all sets, it prints the results of each set. The function does not return any value but modifies an internal list `results` which contains the processed outputs for each test case.

