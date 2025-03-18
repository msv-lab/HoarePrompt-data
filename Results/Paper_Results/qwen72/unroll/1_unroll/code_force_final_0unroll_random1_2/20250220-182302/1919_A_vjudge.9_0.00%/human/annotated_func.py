#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns 'Alice'.
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` within the range 1 to 10^9. It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. The function does not modify the input variables.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. a and b are integers such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: t is an integer input by the user such that 1 <= t <= 1000, a and b are integers such that 1 <= a, b <= 10^9, results is a list containing t elements, each element is the result of the function func_1(a, b) for each iteration.
    for result in results:
        print(result)
        
    #State: The list `results` remains unchanged, and each element in `results` is printed to the console. The variables `t`, `a`, and `b` are not modified by the loop.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user, representing the number of test cases, where `1 <= t <= 1000`. For each test case, it reads two integers `a` and `b` from the user, where `1 <= a, b <= 10^9`. It then calls another function `func_1` with `a` and `b` as arguments, collects the results in a list `results`, and prints each result to the console. The function does not return any value, but it modifies the list `results` to contain the outcomes of `func_1` for each test case. The variables `t`, `a`, and `b` are not modified after their initial input.

