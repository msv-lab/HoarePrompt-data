#State of the program right berfore the function call: No specific variables are present in the function signature of `func_1`. It reads a line of input and returns it as a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers that were read from a line of input, where each integer is obtained by splitting the input line by spaces and converting each split component to an integer.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits the line by spaces, converts each split component to an integer, and returns the result as a list of integers.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: The function `func_3` does not take any arguments and returns a map object that yields integers. This map object is expected to yield at least two integers, where the first integer `n` represents the length of the hidden array and the second integer `k` represents the number of subarrays.
def func_3():
    return map(int, input().split())
    #The program returns a map object that yields integers. The first integer `n` represents the length of the hidden array, and the second integer `k` represents the number of subarrays.
#Overall this is what the function does:The function `func_3` does not accept any arguments and returns a map object that yields integers. The first integer `n` represents the length of the hidden array, and the second integer `k` represents the number of subarrays.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_4` does not take any parameters and returns a string obtained by stripping whitespace from the input.
def func_4():
    return input().strip()
    #The program returns a string obtained by stripping whitespace from the input.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string with leading and trailing whitespace removed from the user's input.

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
        
    #State: `n` and `k` are the values returned by `func_3()`, with `k` being between 1 and `n` (inclusive); `v` is `n` or the value of `i` where `func_2()` returned `n`.
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
        
    #State: `n` and `k` are the values returned by `func_3()`, with `k` being between 1 and `n` (inclusive); `v` is `n` or the value of `i` where `func_2()` returned `n`; `i` is `n // k + 1`; `cnt` is `0`; `l` is a value between `1` and `n + 1`.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_5` does not accept any parameters. It interacts with other functions (`func_3` and `func_2`) to perform a series of operations involving queries and responses, ultimately printing either the value `i * v` if a certain condition is met or `-1` if it is not. The function returns nothing (None).

