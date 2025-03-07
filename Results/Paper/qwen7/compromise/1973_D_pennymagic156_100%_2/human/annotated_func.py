#State of the program right berfore the function call: None of the variables in the provided function have explicit inputs or outputs described. The function `func_1()` reads input from standard input and returns a list of integers obtained from splitting the input string. However, since the problem description and the function signature do not include any variables, we can infer that the function is expected to read inputs for the test cases and split them into integers.
def func_1():
    return list(map(int, input().split()))
    #The program reads a space-separated string of integers as input, splits it, and returns a list of those integers.
#Overall this is what the function does:The function reads a space-separated string of integers from standard input, splits the string into individual integer values, and returns a list containing these integers.

#State of the program right berfore the function call: None of the variables in the function signature are provided, but the function is expected to interact with the user to perform queries and receive responses. The function does not take any parameters and is responsible for handling the input and output as described in the problem statement.
def func_2():
    return int(input())
    #The program waits for user input and returns an integer value entered by the user.
#Overall this is what the function does:The function interacts with the user, waits for an integer input from the user, and returns the entered integer value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, and the values of n and k are read from the input for each test case.
def func_3():
    return map(int, input().split())
    #The program returns a map object that converts the input into integers. The input should be two integers separated by a space, where the first integer is 'n' and the second integer is 'k'.
#Overall this is what the function does:The function reads two integers from the input, where the first integer represents 'n' and the second integer represents 'k'. It then returns a map object that contains these integers.

#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to perform queries and receive responses according to the described problem.
def func_4():
    return input().strip()
    #The program waits for user input and returns the stripped input.
#Overall this is what the function does:The function accepts no parameters and waits for user input. After receiving the input, it removes any leading or trailing whitespace and returns the stripped input.

#State of the program right berfore the function call: (n, k) are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_5():
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: n is a positive integer such that \(1 \leq k \leq n \leq 10^4\), i is 1, and v is \(n - 3\).
    for i in range(1, n // k + 1):
        cnt, l = k, 1
        
        while cnt and l < n + 1:
            print(f'? {l} {i * v}', flush=True)
            l = func_2() + 1
            cnt -= 1
        
        if cnt == 0 and l == n + 1:
            print(f'! {i * v}', flush=True)
            func_2()
            return
        
    #State: After all iterations of the loop, `cnt` is `0`, `l` is `func_2() + 1`, and the condition `(cnt == 0 and l == n + 1)` holds true.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value since there is no return statement with an expression.
#Overall this is what the function does:The function accepts no parameters and performs a series of operations based on the values of `n` and `k`. It prints queries and updates variables `v` and `l` through function calls. If certain conditions are met, it prints a final result and returns `l + 3`. In other cases, it either returns `None` or does not return any value.

