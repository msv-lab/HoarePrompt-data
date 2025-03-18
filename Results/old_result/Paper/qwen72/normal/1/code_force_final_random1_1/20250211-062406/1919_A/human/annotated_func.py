#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns the string 'Alice'.
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` (where 1 <= a, b <= 10^9). It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. The function does not modify the input variables and has no side effects.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, a and b are positive integers such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `t` is 0, `a` and `b` are positive integers provided by the user such that 1 <= a, b <= 10^9, `results` is a list containing `t` values, each value being the result of `func_1(a, b)` for each iteration.
    for result in results:
        print(result)
        
    #State: `t` is at least 1, `results` is a list containing all the values, each of which is the result of `func_1(a, b)` for each iteration.
#Overall this is what the function does:The function `func_2` reads an integer `t` indicating the number of test cases, where `1 <= t <= 1000`. For each test case, it reads two positive integers `a` and `b` (where `1 <= a, b <= 10^9`), calls another function `func_1(a, b)`, and stores the result. After processing all test cases, it prints each result. The final state of the program is that `t` is the number of test cases processed, and the results of `func_1(a, b)` for each test case are printed.

