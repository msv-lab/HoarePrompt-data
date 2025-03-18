#State of the program right berfore the function call: None
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from splitting the input string by spaces and converting each split part into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the user, splits the input string by spaces, converts each resulting substring into an integer, and returns a list of these integers. The final state of the program after the function concludes is that it has a list of integers derived from the user's input.

#State of the program right berfore the function call: None. This function does not take any parameters and simply reads an integer from the standard input.
def func_2():
    return int(input())
    #The program returns an integer value that was input by the user.
#Overall this is what the function does:Reads an integer from the standard input and returns this integer value. The function does not accept any parameters. After the function concludes, the program has returned the integer input by the user.

#State of the program right berfore the function call: None
def func_3():
    return map(int, input().split())
    #The program returns an iterator that yields integer values from the input provided by the user, which is split by spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the user, splits the input by spaces, converts each split part into an integer, and returns an iterator that yields these integer values. The final state of the program includes the returned iterator, which can be used to iterate over the integers derived from the user input.

#State of the program right berfore the function call: None.
def func_4():
    return input().strip()
    #The program returns the input string provided by the user, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters. It reads a line of input from the user, removes any leading and trailing whitespace from the input string, and returns the modified string. After the function concludes, the program has obtained a user-provided string with whitespace trimmed.

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
        
    #State: If the loop completes all iterations without breaking, `i` will be 0, `v` will be the last return value of `func_2()`, and `n` remains unchanged. If the loop breaks early due to `v` equaling `n`, `i` will be the value that caused `v` to equal `n`, and `v` will be set to that `i` value.
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
        
    #State: `i` is 0, `v` is the last return value of `func_2()`, and `n` remains unchanged.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_5` does not accept any parameters and does not return any value. It performs a series of operations involving queries and checks using the functions `func_3` and `func_2`. The function aims to find a specific value `v` by iterating through a range of values and checking conditions. If a certain condition is met, it prints a specific output and terminates. If the condition is not met after all iterations, it prints `! -1` and terminates. The final state of the program is that no value is returned, and the function has printed either a specific value or `! -1`.

