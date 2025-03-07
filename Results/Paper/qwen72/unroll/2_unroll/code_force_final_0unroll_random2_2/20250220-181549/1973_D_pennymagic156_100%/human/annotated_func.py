#State of the program right berfore the function call: This function does not take any arguments and is used to read input from the user, which is expected to be a line of space-separated integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is derived from the space-separated integers input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of space-separated integers from the user and returns a list of integers derived from this input. The final state of the program after the function concludes is that it has a list of integers, assuming the user input was valid. If the user input is not a valid sequence of space-separated integers, the function will raise a `ValueError`.

#State of the program right berfore the function call: None.
def func_2():
    return int(input())
    #The program returns an integer value provided by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value provided by the user. After the function concludes, the program state includes the returned integer value, which is the result of the user's input.

#State of the program right berfore the function call: No variables are used in the function signature.
def func_3():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a map object that converts each element of an input string, split by spaces, into an integer. The input string is read from the user via the `input()` function. After the function call, the program has a map object that can be iterated over to access the converted integers.

#State of the program right berfore the function call: None.
def func_4():
    return input().strip()
    #The program returns the input string after removing leading and trailing whitespace.
#Overall this is what the function does:The function `func_4` accepts no parameters and returns a string obtained from user input after removing any leading and trailing whitespace. The function does not modify any external state or variables.

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
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `v` is the largest integer `i` in the range [1, n] for which `func_2()` returns `n`. If no such `i` exists, `v` remains 1.
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
        
    #State: `i = n // k`, `cnt = 0`, `l = n + 1`.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_5` does not accept any parameters and does not return any value. It interacts with external functions `func_3` and `func_2` to determine a specific value `v` and then performs a series of queries. If a suitable value `v` is found, it prints a final result of the form `! {i * v}` where `i` is a multiple of `v` that satisfies certain conditions. If no suitable value is found, it prints `! -1`. The function always ends by calling `func_2()`.

