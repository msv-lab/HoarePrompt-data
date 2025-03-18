#State of the program right berfore the function call: None of the variables in the function `func_1()` are provided in the function signature. However, the function reads input from standard input, which consists of multiple test cases. Each test case starts with an integer `t` indicating the number of test cases, followed by pairs of integers `n` and `k` for each test case. The input format is structured as described in the problem statement.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from standard input, where each pair of integers `n` and `k` is split and converted to integers.
#Overall this is what the function does:The function reads a series of test cases from standard input, each starting with an integer `t` indicating the number of subsequent pairs of integers `n` and `k`. For each pair, it converts `n` and `k` to integers and collects them into a list. Finally, it returns this list of integers.

#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to make queries and receive responses. The function does not take any parameters and is expected to handle the input and output as described in the problem statement.
def func_2():
    return int(input())
    #The program waits for user input and returns an integer value entered by the user.
#Overall this is what the function does:The function waits for the user to input an integer value and then returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, l and x are integers such that 1 ≤ l ≤ n and 1 ≤ x ≤ 10^9, and r is an integer representing the smallest integer such that l ≤ r ≤ n and f(l, r) = x, or n + 1 if no such r exists.
def func_3():
    return map(int, input().split())
    #The program returns a tuple of four integers (t, n, k, r) where t is an integer between 1 and 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, and r is an integer representing the smallest integer such that l ≤ r ≤ n and f(l, r) = x, or n + 1 if no such r exists.
#Overall this is what the function does:The function reads four integers from the standard input, splits them into a tuple, and returns it. The tuple contains integers \( t \), \( n \), \( k \), and \( r \), where \( t \) ranges from 1 to 10^3, \( n \) and \( k \) satisfy \( 1 \leq k \leq n \leq 10^4 \), and \( r \) represents the smallest integer such that \( l \leq r \leq n \) and \( f(l, r) = x \), or \( n + 1 \) if no such \( r \) exists.

#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to make queries and receive responses according to the described interaction protocol.
def func_4():
    return input().strip()
    #The program returns the user's input after stripping any trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and prompts the user to enter some input. It then strips any trailing whitespace from the input and returns the modified input to the caller.

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
        
    #State: v is the return value of `func_2()` after the last iteration, `n` is 1 (since the loop decrements `i` from `n` to 1), `k` is the return value of `func_3()`, and `i` is 0 (as the loop runs until `i` reaches 1 and then decrements again).
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
        
    #State: i is 0, n is 1, k must be 1, cnt is 0, l is func_2() + 1.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value since there is no value being returned in the provided code snippet.
#Overall this is what the function does:The function does not accept any parameters and does not return any value. It performs a series of operations involving loops and function calls (`func_2` and `func_3`). Specifically, it prints queries and processes responses from `func_2`, aiming to find a specific condition where it can terminate early or continue until a certain count reaches zero. If a valid condition is met, it prints a result; otherwise, it prints `-1`.

