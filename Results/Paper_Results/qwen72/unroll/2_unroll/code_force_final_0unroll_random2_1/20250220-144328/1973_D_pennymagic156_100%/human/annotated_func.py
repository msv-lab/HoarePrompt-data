#State of the program right berfore the function call: None
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers converted from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns a list of integers. The input string is read from the user, split by spaces, and each substring is converted to an integer. The final state of the program after the function call is that it has a list of integers derived from the user input.

#State of the program right berfore the function call: None
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is input by the user. The state of the program after the function concludes is that the user's input has been converted to an integer and is returned.

#State of the program right berfore the function call: No specific variables are used in the function signature.
def func_3():
    return map(int, input().split())
    #The program returns an iterator that yields integer values from the input provided by the user, where the input is a string of space-separated numbers.
#Overall this is what the function does:The function `func_3` accepts no parameters and returns an iterator that yields integer values from a string of space-separated numbers provided by the user. The user's input is split into individual number strings, and each string is converted to an integer. The final state of the program after the function concludes is that the function has returned an iterator, and the user can iterate over this iterator to access the integer values.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_4():
    return input().strip()
    #The program returns the input string after removing any leading and trailing whitespace characters.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string obtained from user input, with any leading and trailing whitespace characters removed.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
def func_5():
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: `n` and `k` remain unchanged, `v` is the value of `i` when `v == n` for the first time, or `v` is 1 if no such `i` is found.
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
        
    #State: `i` is the value at which the loop returns, `cnt` is 0, `l` is `n + 1`, and `v` remains unchanged.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_5` performs a series of queries using `func_2` and `func_3`. It first determines a value `v` by iterating from `n` down to 1, checking if the result of `func_2` equals `n`. If found, `v` is set to the corresponding `i`; otherwise, `v` remains 1. It then iterates from 1 to `n // k + 1`, performing additional queries and checking conditions. If a specific condition is met, it prints a result and calls `func_2` before returning. If no such condition is met, it prints `! -1` and calls `func_2` before returning. The function does not accept any parameters and does not return any output.

