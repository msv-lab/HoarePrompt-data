#State of the program right berfore the function call: None. The function does not take any parameters.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers entered by the user, where the integers are separated by spaces.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the user, splits the input by spaces, converts each split part into an integer, and returns a list of these integers. The final state of the program after the function concludes is that the user's input has been transformed into a list of integers, and this list is returned.

#State of the program right berfore the function call: No variables are passed to the function, and the function reads an integer from the standard input.
def func_2():
    return int(input())
    #The program returns the integer value entered by the user through standard input.
#Overall this is what the function does:The function `func_2` reads an integer from the standard input and returns this integer value. After the function concludes, the program has no side effects and the returned value is the integer entered by the user.

#State of the program right berfore the function call: None
def func_3():
    return map(int, input().split())
    #The program returns a map object that contains the integer values obtained from splitting the user input by spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a map object containing integer values obtained from splitting the user input by spaces. The user input is expected to be a string of space-separated numbers. After the function concludes, the map object can be iterated over to access the integer values.

#State of the program right berfore the function call: None
def func_4():
    return input().strip()
    #The program returns the input string provided by the user, with any leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the input string provided by the user with any leading and trailing whitespace removed.

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
        
    #State: `n` and `k` are positive integers such that 1 <= k <= n <= 10^4, `v` is the largest integer `i` such that `i * n` results in `n` when passed to `func_2()`. If no such `i` is found, `v` remains 1.
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
        
    #State: The loop will print a series of queries in the format `? l i*v` for each valid `l` and `i*v` combination, and if the conditions are met, it will print a final statement `! i*v` and return. The variables `n`, `k`, and `v` will remain unchanged, while `i` will be the last value in the range `1` to `n // k` that was processed, `cnt` will be `0`, and `l` will be `n + 1`.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns without any value.
#Overall this is what the function does:The function `func_5` interacts with two other functions, `func_3` and `func_2`, to perform a series of queries and potentially print a final result. It starts by obtaining two positive integers `n` and `k` from `func_3` such that `1 <= k <= n <= 10^4`. It then searches for the largest integer `i` in the range `[1, n]` such that `i * n` results in `n` when passed to `func_2`. If such an `i` is found, `v` is set to this value; otherwise, `v` remains 1. Next, the function iterates over a range from `1` to `n // k` and for each value of `i` in this range, it performs a series of queries in the format `? l i*v` where `l` starts from 1 and increments by the value returned by `func_2` + 1 until `l` reaches `n + 1` or the count `cnt` reaches 0. If the conditions are met, it prints a final statement `! i*v` and returns. If no such conditions are met, it prints `! -1` and returns. The function does not return any value.

