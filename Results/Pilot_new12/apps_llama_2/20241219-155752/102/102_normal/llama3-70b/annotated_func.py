#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n <= 10,000,000, 1 <= a <= 10,000,000, and 1 <= b <= 10,000,000.
def func():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        y = (n - x * a) // b
        
        if x * a + y * b == n:
            print('YES')
            print(x, y)
            exit()
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a non-zero input integer, `b` is an input integer, `x` is `n // a`, `y` is `(n - x * a) // b` if the loop completes without finding a solution (`x * a + y * b = n`), indicating no integer solution was found within the given constraints. If a solution was found, the program would have exited with 'YES' and the specific `x` and `y` values that satisfy `x * a + y * b = n`.
    print('NO')
#Overall this is what the function does:The function determines whether it is possible to express a given integer `n` as a linear combination of two other integers `a` and `b`, both ranging from 1 to 10,000,000, with non-negative integer coefficients. It takes no parameters but reads three integers from standard input: `n`, `a`, and `b`. If such a combination exists, it outputs 'YES' followed by the coefficients `x` and `y` that satisfy the equation `x * a + y * b = n`. If no such combination is found, it outputs 'NO'. The function does not return any value but instead prints the result directly to the console, effectively terminating the program upon finding a solution or exhausting all possibilities. The function's primary action is to check for integer solutions within the specified constraints, and its final state is either having printed a solution and exited or having indicated that no solution exists.

