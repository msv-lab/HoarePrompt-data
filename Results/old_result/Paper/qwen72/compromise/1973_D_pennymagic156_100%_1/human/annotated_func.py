#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from stdin, typically for interactive problems where the input format is known.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string from stdin and converting each split part into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from standard input (stdin), splits the input string into parts based on whitespace, converts each part into an integer, and returns a list of these integers. After the function concludes, the program has a list of integers derived from the input.

#State of the program right berfore the function call: None. This function does not take any parameters and simply reads an integer from the standard input.
def func_2():
    return int(input())
    #The program returns an integer value read from the standard input.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer value from the standard input and returns this integer value. After the function concludes, the program has read an integer from the user and the returned value is the integer that was input.

#State of the program right berfore the function call: No variables are passed to the function.
def func_3():
    return map(int, input().split())
    #The program returns an iterator that yields integer values from the input provided by the user, where the input is split by whitespace.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the user, splits the input by whitespace, converts each split part into an integer, and returns an iterator that yields these integer values. After the function concludes, the caller will have an iterator that can be used to iterate over the integers derived from the user's input.

#State of the program right berfore the function call: None.
def func_4():
    return input().strip()
    #The program returns the input string after stripping leading and trailing whitespace.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string obtained from user input after removing any leading and trailing whitespace.

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
        
    #State: If the loop completes all iterations without breaking, `i` will be 0 (since the loop decrements `i` from `n` to 1, and the loop condition is `i > 0`). The value of `v` will be the last return value of `func_2()` unless `v` was set to `n` during one of the iterations, in which case `v` will be the value of `i` at that iteration. The values of `n` and `k` remain unchanged as they are not modified within the loop.
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
        
    #State: `i` is 0, `n` remains unchanged, `k` remains unchanged, `cnt` is 0, `l` is `func_2() + 1` (where `func_2()` is less than `n`), and `v` is the last value of `i * v` printed before the loop exits.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_5` interacts with external functions `func_2` and `func_3` to perform a series of queries and operations. It does not accept any parameters and does not return any value. The function initializes `n` and `k` using `func_3`, and then iterates through a loop to find a specific value `v`. If a certain condition is met, it performs additional queries and prints a result. If the conditions are not met, it prints `-1`. Throughout its execution, the function prints formatted strings to the console and calls `func_2` multiple times. The final state of the program includes the unchanged values of `n` and `k`, and the printed output based on the logic executed.

