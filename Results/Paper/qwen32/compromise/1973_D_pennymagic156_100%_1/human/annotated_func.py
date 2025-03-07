#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters and returns a list of integers obtained from the standard input.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from the standard input.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into components based on whitespace, converts each component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. Therefore, no specific precondition can be derived from the variables in the function signature.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: No variables are present in the function signature. This function does not contribute directly to the solution but seems to be a utility function for reading input values, which are expected to be two integers.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing two integers that were read from the input and split by whitespace.
#Overall this is what the function does:The function `func_3` reads a line of input, splits it into two parts based on whitespace, converts each part into an integer, and returns a map object containing these two integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_4`. Therefore, no specific precondition can be derived from the variables.
def func_4():
    return input().strip()
    #The program returns the input string with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string with leading and trailing whitespace removed.

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
        
    #State: `n` and `k` are the values returned by `func_3()`, `i` is `1`, and `v` is the value returned by `func_2()` in the last iteration.
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
        
    #State: `i` is `n // k + 1`, `cnt` is the last value of `cnt` from the last iteration, and `l` is the last value of `l` from the last iteration.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_5` takes no direct input parameters but retrieves two positive integers `n` and `k` (where 1 ≤ k ≤ n ≤ 10^4) from another function `func_3`. It then performs a series of operations involving printing queries and receiving responses through `func_2`. Based on these interactions, it either prints a specific value followed by calling `func_2` and returning `None`, or it prints '! -1' followed by calling `func_2` and returning `None`. The function does not modify its input parameters and does not return any meaningful value.

