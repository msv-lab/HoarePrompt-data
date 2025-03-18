#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns 'Bob'
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (both between 1 and 10^9). It checks if their sum is even. If the sum is even, it returns 'Bob'; otherwise, it returns 'Alice'.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: Output State: `t` is an integer between 1 and 1000 inclusive; `results` is a list containing 1000 elements, where each element is the result of calling `func_1(a, b)` for each iteration of the loop with `a` and `b` being integers provided by user input.
    for result in results:
        print(result)
        
    #State: The variable `t` remains unchanged as an integer between 1 and 1000 inclusive; the `results` list contains the same 1000 elements, which are the results of calling `func_1(a, b)` for each iteration of the loop with `a` and `b` being integers provided by user input. The loop simply prints each element in the `results` list without modifying it.
#Overall this is what the function does:The function processes a specified number of test cases, where each test case consists of two positive integers \(a\) and \(b\). For each test case, it calls another function `func_1(a, b)` to determine the result. It collects these results in a list and then prints each result. The function does not modify the input integer \(t\) (the number of test cases) and ensures that the final output is a list of results corresponding to each test case.

