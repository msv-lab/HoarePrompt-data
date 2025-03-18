#State of the program right berfore the function call: None. This function does not take any parameters. It reads input from stdin and returns a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by reading a line of input from stdin, splitting it into separate strings based on spaces, and converting each string into an integer.
#Overall this is what the function does:The function `func_1` reads a line of input from standard input (stdin), splits the line into separate strings based on spaces, converts each string into an integer, and returns a list of these integers. The function does not accept any parameters and does not modify any external state. After the function concludes, the program has a list of integers derived from the input.

#State of the program right berfore the function call: None. This function does not take any parameters and simply reads an integer from the standard input.
def func_2():
    return int(input())
    #The program returns an integer value that was read from the standard input.
#Overall this is what the function does:The function `func_2` reads an integer value from the standard input and returns this integer value. It does not accept any parameters. After the function concludes, the program has read an integer from the user and the returned value is the integer that was input.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from the user, which is expected to be a line of space-separated integers.
def func_3():
    return map(int, input().split())
    #The program returns an iterator that converts each element of the user's input (expected to be a line of space-separated integers) into an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of space-separated integers from the user and returns an iterator that converts each element of the input into an integer. After the function concludes, the program has an iterator that can be used to access the converted integers.

#State of the program right berfore the function call: None
def func_4():
    return input().strip()
    #The program returns the stripped input provided by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters. It reads a line of input from the user, strips any leading and trailing whitespace, and returns the resulting string. The final state of the program after the function concludes is that the user-provided input, with leading and trailing whitespace removed, is returned.

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
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `v` is the value of `i` when `v` equals `n` or 1 if no such `i` exists, and `i` is 0.
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
        
    #State: After the loop executes all iterations, `n` and `k` are positive integers such that \( 1 \leq k \leq n \leq 10^4 \), `v` is the value of `i` when `v` equals `n` or 1 if no such `i` exists, `i` is `n // k`, `cnt` is 0, `l` is `func_2() + 1` and `l < n + 1`. Additionally, either `cnt` is not 0 or `l` is not equal to `n + 1`. The loop will have printed `! {i * v}` where `i` is the last value of `i` before the loop terminates.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value. It prints `! {i * v}` where `i` is the last value of `i` before the loop terminates, and `v` is the value of `i` when `v` equals `n` or 1 if no such `i` exists.
#Overall this is what the function does:The function `func_5` does not accept any parameters directly but operates with two positive integers `n` and `k` (where 1 <= k <= n <= 10^4) obtained from the function `func_3`. It does not return any value. The function performs a series of queries and prints specific outputs based on the results of these queries. If a condition is met, it prints `! {i * v}`, where `i` is the last value of `i` before the loop terminates, and `v` is the value of `i` when `v` equals `n` or 1 if no such `i` exists. If the condition is not met, it prints `! -1`.

