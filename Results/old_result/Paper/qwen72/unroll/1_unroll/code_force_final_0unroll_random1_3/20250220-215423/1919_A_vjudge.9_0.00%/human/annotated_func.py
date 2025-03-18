#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns 'Alice'.
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` (1 <= a, b <= 10^9). It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. The function does not modify the input variables.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `t` is the input integer provided by the user, where 1 <= t <= 1000; `results` is a list containing `t` elements, each element being the result of the function `func_1(a, b)` for the corresponding iteration.
    for result in results:
        print(result)
        
    #State: The loop has printed each element in the `results` list, one by one, and the `results` list remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It prompts the user to enter a number of test cases `t` (where 1 <= t <= 1000). For each test case, it reads two integers `a` and `b` from the user, calls the function `func_1(a, b)`, and stores the result in a list. After processing all test cases, it prints each result in the list, one by one. The function does not return any value.

