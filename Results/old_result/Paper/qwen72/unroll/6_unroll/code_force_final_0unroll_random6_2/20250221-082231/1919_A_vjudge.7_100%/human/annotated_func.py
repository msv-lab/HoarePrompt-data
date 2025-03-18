#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9. Additionally, the function should be designed to handle multiple test cases, where the number of test cases t is an integer such that 1 <= t <= 1000.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has finished executing all iterations. The values of `a` and `b` are not retained after each iteration, and the variable `t` has been incremented from 0 to `test - 1`. The output for each iteration is either 'Bob' or 'Alice' based on the condition `(a + b) % 2 == 0`.
#Overall this is what the function does:The function `func` reads an integer `test` indicating the number of test cases (1 <= test <= 1000). For each test case, it reads two integers `a` and `b` (1 <= a, b <= 10^9) from the input. It then checks if the sum of `a` and `b` is even. If the sum is even, it prints 'Bob'; otherwise, it prints 'Alice'. After processing all test cases, the function concludes without returning any value. The final state of the program is that the loop has completed, and the output for each test case has been printed to the console.

