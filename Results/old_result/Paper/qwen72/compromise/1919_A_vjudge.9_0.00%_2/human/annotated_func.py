#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` (where 1 <= a, b <= 10^9) and returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. After the function concludes, it will have returned one of these two strings, and the input variables `a` and `b` remain unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `results` is a list containing `t` elements, where each element is the result of the function `func_1(a, b)` for the corresponding iteration.
    for result in results:
        print(result)
        
    #State: The list `results` remains unchanged, and each element of `results` is printed to the console in the order they appear in the list.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It prompts the user to enter the number of test cases, `t`, where `1 <= t <= 1000`. For each test case, it reads two integers `a` and `b` from the user, calls the function `func_1(a, b)`, and stores the result in a list `results`. After processing all test cases, it prints each element of the `results` list to the console in the order they were added. The list `results` remains unchanged after the function concludes.

