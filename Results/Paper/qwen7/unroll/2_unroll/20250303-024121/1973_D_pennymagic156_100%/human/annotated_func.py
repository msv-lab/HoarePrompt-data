#State of the program right berfore the function call: None of the variables in the function signature are provided. However, the function is expected to interact with the user to perform queries and receive responses. The function reads input from standard input and outputs to standard output.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers that the user inputs separated by spaces.
#Overall this is what the function does:The function reads a line of input from the user, splits it into a list of integers based on spaces, and returns this list.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, l and x are integers such that 1 ≤ l ≤ n and 1 ≤ x ≤ 10^9, and r is an integer representing the smallest positive integer r such that f(l, r) = x, or n+1 if no such r exists.
def func_2():
    return int(input())
    #The program returns an integer input by the user, which is the value of r such that f(l, r) = x, or n+1 if no such r exists.
#Overall this is what the function does:The function prompts the user to input an integer, which represents the value of \( r \) such that \( f(l, r) = x \), or \( n+1 \) if no such \( r \) exists. The function then returns this integer input by the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, l and x are integers such that 1 ≤ l ≤ n and 1 ≤ x ≤ 10^9, and r is an integer as the answer to the query.
def func_3():
    return map(int, input().split())
    #The program returns a tuple of integers (t, n, k, l, x) where t is an integer such that 1 ≤ t ≤ 10^3, n and k are integers such that 1 ≤ k ≤ n ≤ 10^4, l and x are integers such that 1 ≤ l ≤ n and 1 ≤ x ≤ 10^9, and r is not returned as it is not part of the input.
#Overall this is what the function does:The function reads five integers from standard input, which must be formatted as a space-separated line. These integers represent \( t \) (1 ≤ \( t \) ≤ 10^3), \( n \) (1 ≤ \( k \) ≤ \( n \) ≤ 10^4), \( k \), \( l \) (1 ≤ \( l \) ≤ \( n \)), and \( x \) (1 ≤ \( x \) ≤ 10^9). It then returns these values as a tuple (t, n, k, l, x).

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, n and k are integers such that 1 <= k <= n <= 10^4, and the values of l and x are integers where 1 <= l <= n and 1 <= x <= 10^9.
def func_4():
    return input().strip()
    #The program returns a string input by the user after stripping any trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns a string input by the user after stripping any trailing whitespace.

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
        
    #State: v is the smallest integer greater than or equal to n/2, n is the return value of func_3(), k is the return value of func_3().
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
        
    #State: Output State: v is the smallest integer greater than or equal to n/2, n is the return value of func_3(), k is the return value of func_3(), i is the last iteration value of the for loop, cnt is 0, l is n + 1.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be set to the last value it took during the loop's execution, which is `n // k`. The variables `cnt` and `l` inside the inner while loop are reset to 0 and n+1 respectively when the condition `cnt == 0 and l == n + 1` is met, and the corresponding print statement `! {i * v}` is executed. This means that after the loop finishes, `cnt` will be 0 and `l` will be n + 1, and the loop will exit. The values of `v`, `n`, and `k` remain unchanged as they are not modified within the loop.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns None
#Overall this is what the function does:The function accepts no parameters and returns None. It first initializes variables `n` and `k` using the result of `func_3()`. It then iterates from `n` down to 1, updating `v` based on the result of `func_2()`. If `v` equals `n`, it breaks the loop and sets `v` to the current value of `i`. Next, it enters another loop that iterates from 1 to `n // k`, performing a series of operations involving `func_2()` and printing results. If certain conditions are met, it prints a final result and returns. If no conditions are met, it prints '! -1' and returns.

