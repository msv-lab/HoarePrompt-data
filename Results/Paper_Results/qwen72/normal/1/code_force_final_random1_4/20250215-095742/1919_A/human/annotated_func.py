#State of the program right berfore the function call: a and b are integers such that 1 <= a, b <= 10^9.
def func_1(a, b):
    if ((a + b) % 2 == 0) :
        return 'Bob'
        #The program returns the string 'Bob'.
    else :
        return 'Alice'
        #The program returns 'Alice'.
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` within the range 1 to 10^9. It returns 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. After the function concludes, the program will have returned one of these two strings based on the parity of the sum of `a` and `b`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, a and b are positive integers such that 1 <= a, b <= 10^9.
def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        a, b = map(int, input().strip().split())
        
        winner = func_1(a, b)
        
        results.append(winner)
        
    #State: After the loop has executed all its iterations, `t` must be greater than or equal to the number of iterations that were specified initially. `results` is a list containing `t` elements, where each element is the result of `func_1(a, b)` for each iteration. For each iteration, `a` and `b` are updated with new integer values from user input, and `winner` holds the result of `func_1(a, b)` for the last iteration. The values of `a` and `b` are the last set of integers provided by the user input, and `winner` is the result of `func_1(a, b)` using these last values.
    for result in results:
        print(result)
        
    #State: `results` is a list containing `t` elements, where `t` is the total number of iterations specified initially. Each element in `results` is the result of `func_1(a, b)` for each iteration. `a` and `b` hold the last set of integers provided by the user input, and `winner` holds the result of `func_1(a, b)` using these last values.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user, representing the number of test cases, where `1 <= t <= 1000`. For each test case, it reads two integers `a` and `b` from the user, where `1 <= a, b <= 10^9`. It then calls another function `func_1` with `a` and `b` as arguments and stores the result in a list `results`. After processing all test cases, it prints each result in the list `results`. The final state of the program is that `results` contains `t` elements, each being the result of `func_1(a, b)` for the corresponding test case, and the values of `a` and `b` are the last set of integers provided by the user.

