#State of the program right berfore the function call: None of the variables in the function signature are provided, but based on the problem description and the context, the function does not take any parameters. It reads input from standard input and returns a list of integers representing the values of n and k.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string on spaces and converting each part to an integer.
#Overall this is what the function does:The function reads a line of space-separated integers from standard input and returns them as a list of integers.

#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to perform queries and receive responses. The function should handle the following operations:
def func_2():
    return int(input())
    #The program waits for user input and returns an integer value entered by the user.
#Overall this is what the function does:The function interacts with the user to wait for an integer input and returns the entered integer value.

#State of the program right berfore the function call: None of the variables in the function `func_3()` are provided in the function signature. However, the function is expected to read input from the standard input and return a tuple of two integers. The input format is guaranteed to be two space-separated integers representing the number of test cases and the values within each test case as described in the problem statement.
def func_3():
    return map(int, input().split())
    #The program reads two space-separated integers from the standard input and returns them as a tuple.
#Overall this is what the function does:The function reads two space-separated integers from the standard input and returns them as a tuple.

#State of the program right berfore the function call: **
def func_4():
    return input().strip()
    #The program returns the user's input after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns the user's input after stripping any leading or trailing whitespace.

#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_5():
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: n is a positive integer, k is a positive integer such that 1 ≤ k ≤ n ≤ 10^4, and v is either i or n depending on whether v equals n during the loop execution.
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
        
    #State: v is n, cnt is 0, l is n + 1 for each iteration of the outer loop, and the inner loop prints ? l i * v for each valid l from 1 to n.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value since there is no return statement in the provided code snippet.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, both of which are positive integers with the constraint \(1 \leq k \leq n \leq 10^4\). It then performs a series of operations involving printing queries and processing responses. If certain conditions are met, it prints a final answer and terminates. Otherwise, it prints `-1` and ends. The function does not return any value.

