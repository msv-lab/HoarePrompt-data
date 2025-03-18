#State of the program right berfore the function call: No specific variables are present in the function signature of `func_1`. However, based on the context, `func_1` is expected to return a list of integers, likely representing the input values for a test case, such as `n` and `k` or elements of the hidden array `a`.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string and converting each split substring to an integer.
#Overall this is what the function does:The function `func_1` takes no input parameters and returns a list of integers by reading a line of input, splitting it into substrings, and converting each substring to an integer.

#State of the program right berfore the function call: No specific variables are provided in the function signature, thus the precondition is not applicable based on the given function.
def func_2():
    return int(input())
    #The program returns the integer value that is input by the user.
#Overall this is what the function does:The function `func_2` prompts the user for input, converts that input to an integer, and returns this integer value.

#State of the program right berfore the function call: No specific variables are present in the function signature `func_3()`. This function is expected to read and return two integers from the input.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing two integers that were read from the input.
#Overall this is what the function does:The function `func_3` reads two integers from the input and returns a map object containing these two integers.

#State of the program right berfore the function call: No variables are present in the function signature, so no precondition can be derived from it.
def func_4():
    return input().strip()
    #The program returns the input string with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string with leading and trailing whitespace removed, based on user input.

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
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, v is the value returned by func_2() in the last iteration.
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
        
    #State: n is a positive integer, k is a positive integer such that 1 <= k <= n, v is the value returned by func_2() in the last iteration, cnt is 0, l is n + 1, and i is the value that caused the loop to terminate.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_5` performs a series of queries to determine a specific value based on the input parameters `n` and `k`, which are obtained from `func_3`. It then uses another function `func_2` to process the results of these queries. If a valid value is found that satisfies certain conditions, it prints this value. If no such value is found, it prints `-1`. The function itself does not return any value (None).

