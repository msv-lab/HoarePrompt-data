#State of the program right berfore the function call: No variables in the function signature. This function likely serves to read input values for the problem, specifically a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers that were input by the user, separated by spaces.
#Overall this is what the function does:The function reads a line of input from the user, splits it by spaces, converts each split string into an integer, and returns a list of these integers.

#State of the program right berfore the function call: No explicit variables are present in the function signature of `func_2()`. Therefore, no specific precondition can be derived from the signature alone.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` accepts no parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: No variables are used in the function signature of `func_3`. Therefore, there is no precondition based on the function signature alone.
def func_3():
    return map(int, input().split())
    #The program returns a map object that contains integers derived from the input string, where the input string is split by whitespace.
#Overall this is what the function does:The function `func_3` takes no input parameters, reads a line of input from the user, splits it into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_4` does not take any parameters and returns a string which is the result of `input().strip()`.
def func_4():
    return input().strip()
    #The program returns a string which is the result of `input().strip()`.
#Overall this is what the function does:The function `func_4` prompts the user for input, removes any leading and trailing whitespace from the input, and returns the resulting string.

#State of the program right berfore the function call: n is a positive integer representing the length of the hidden array, and k is a positive integer such that 1 <= k <= n.
def func_5():
    n, k = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        
        v = func_2()
        
        if v == n:
            v = i
            break
        
    #State: `n` and `k` are the values returned by `func_3()`, and `k` satisfies 1 <= `k` <= `n`; `v` is either the value of `i` when `func_2()` returns `n`, or 1 if `func_2()` never returns `n`.
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
        
    #State: `i` is the value that caused the loop to exit, `cnt` is 0, `l` is `n + 1`, `v` is either the value of `i` when `func_2()` returns `n`, or `1` if `func_2()` never returns `n`.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_5` interacts with an external process by sending queries and receiving responses. It uses these interactions to determine a specific value `i * v` based on the conditions defined by the responses. If such a value is found, it outputs `! i * v`. If no such value is found after a series of queries, it outputs `! -1`. The function does not return any value (None).

