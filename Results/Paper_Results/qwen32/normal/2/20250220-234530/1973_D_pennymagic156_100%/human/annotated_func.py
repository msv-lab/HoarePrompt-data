#State of the program right berfore the function call: No specific variables are present in the function signature of `func_1`. It reads a line of input and returns a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers derived from the input line, where each integer is obtained by splitting the input line by spaces and converting each split component into an integer.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits the line by spaces, converts each split component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: No specific variables are present in the function signature provided. The function `func_2` does not take any parameters and returns an integer, which implies it likely reads input from an external source (possibly standard input) and processes it to return an integer value.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` prompts the user for input, reads an integer from the input, and returns that integer.

#State of the program right berfore the function call: No specific variables are provided in the function signature of `func_3`. It appears to be a utility function that reads a line of input and returns the space-separated integers as a map object. No direct relationship between variables can be described as there are none in the signature.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing space-separated integers from the input line.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, splits it into space-separated components, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No specific variables are provided in the function signature of `func_4()`. It appears to be a placeholder function that reads input without parameters.
def func_4():
    return input().strip()
    #The program returns the stripped version of the user's input.
#Overall this is what the function does:The function `func_4` reads a line of input from the user and returns it with any leading and trailing whitespace removed.

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
        
    #State: `i` is 0 if the loop completes all iterations without breaking, otherwise `i` is the value just before the break; `v` is the last value returned by `func_2()` if the loop completes all iterations without breaking, otherwise `v` is the value of `i` when `v` equals `n`; `n` and `k` remain unchanged.
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
        
    #State: `i` is `n // k + 1`, `v` remains unchanged, `n` remains unchanged, `k` remains unchanged.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_5` takes no direct input parameters but internally retrieves two positive integers `n` and `k` (where 1 <= k <= n <= 10^4) from another function `func_3`. It performs a series of operations involving interactions with other functions (`func_2`) and prints specific queries and results based on these interactions. Ultimately, it either prints a result in the form of `! <value>` or `! -1` and does not return any value.

