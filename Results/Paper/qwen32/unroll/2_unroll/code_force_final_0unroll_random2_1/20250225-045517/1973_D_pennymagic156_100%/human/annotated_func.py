#State of the program right berfore the function call: The function `func_1` does not take any parameters and returns a list of integers, which are the values obtained by splitting a line of input into individual integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting a line of input into individual integers.
#Overall this is what the function does:The function `func_1` reads a line of input, splits it into individual components, converts each component to an integer, and returns a list of these integers.

#State of the program right berfore the function call: No specific variables are mentioned in the function signature of `func_2()`. It does not take any parameters and returns an integer, which is expected to be provided as input during the function call.
def func_2():
    return int(input())
    #The program returns an integer that is provided as input during the function call.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer that is provided as input during the function call.

#State of the program right berfore the function call: The function `func_3` does not take any parameters and returns a map object which is an iterator of integers obtained by splitting a line of input.
def func_3():
    return map(int, input().split())
    #The program returns a map object which is an iterator of integers obtained by splitting a line of input.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, splits it into substrings based on whitespace, converts each substring into an integer, and returns a map object which is an iterator of these integers.

#State of the program right berfore the function call: No variables are used in the function signature of `func_4`.
def func_4():
    return input().strip()
    #The program returns the input string with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string with leading and trailing whitespace removed.

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
        
    #State: n, k, and v (where v is the value of i for which func_2() returned n).
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
        
    #State: n, k, v.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing (None).
#Overall this is what the function does:The function accepts no direct parameters but retrieves two positive integers `n` and `k` (where `1 <= k <= n <= 10^4`) from `func_3()`. It performs a series of operations involving calls to `func_2()` and prints specific queries based on the values of `n`, `k`, and a derived value `v`. The function ultimately prints either `! i * v` if a certain condition is met or `! -1` if the condition is not met, and then returns `None`.

