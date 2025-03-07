#State of the program right berfore the function call: a and b are positive integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns the string 'Alice'.
#Overall this is what the function does:The function `func_1` accepts two positive integers `a` and `b` (where 1 <= a, b <= 10^9). It checks if the sum of `a` and `b` is even. If the sum is even, it returns the string 'Bob'. If the sum is odd, it returns the string 'Alice'. After the function concludes, it will have returned either 'Bob' or 'Alice' based on the parity of the sum of `a` and `b`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, a and b are positive integers such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `t` must be greater than or equal to the number of iterations, `_` is a throwaway variable, `results` is a list containing the results of `func_1(a, b)` for each iteration, `a` and `b` are positive integers such that 1 <= a, b <= 10^9, and they are set to the input values for the last iteration, `winner` is the result of `func_1(a, b)` for the last iteration.
    for result in results:
        print(result)
        
    #State: `results` is a list containing all the results from `func_1(a, b)` for each iteration, and the loop has printed each result in `results` exactly once.
#Overall this is what the function does:The function `func_2` reads an integer `t` representing the number of test cases, where `1 <= t <= 1000`. For each test case, it reads two positive integers `a` and `b` (where `1 <= a, b <= 10^9`), and calls another function `func_1(a, b)` to determine a winner. The results of these calls are stored in a list `results`. After processing all test cases, the function prints each result in `results` exactly once. The final state of the program is that `results` contains the outcomes of `func_1(a, b)` for each test case, and these outcomes have been printed to the console.

