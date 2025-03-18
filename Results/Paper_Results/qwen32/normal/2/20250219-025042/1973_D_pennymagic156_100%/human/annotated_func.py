#State of the program right berfore the function call: No specific variables are present in the function signature `func_1`. It does not contribute to defining any preconditions based on the provided signature alone. However, given the context, it reads a line of input and returns it as a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers derived from the input line, where each element in the list corresponds to an integer from the input separated by spaces.
#Overall this is what the function does:The function `func_1` reads a line of input from the user, splits the line into components based on spaces, converts each component into an integer, and returns a list of these integers.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: No specific variables are provided in the function signature of `func_3`. It appears to be a utility function that reads a line of input and returns the space-separated integers as a map object.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing space-separated integers from the input line.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, splits it into space-separated parts, converts each part into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No specific variables are provided in the function signature of `func_4`. It appears to be a placeholder function that reads input without parameters.
def func_4():
    return input().strip()
    #The program returns the user's input as a string with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` reads a line of input from the user, removes any leading and trailing whitespace from the input, and returns the resulting string.

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
        
    #State: `n` is a positive integer, `k` is an integer such that `1 <= k <= n`, and `v` is the value returned by `func_2()` during the last iteration (`i = 1`). If `v` equals `n`, `v` is set to `1` and the loop breaks; otherwise, `v` remains the value returned by `func_2()` and `i` is `1`.
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
        
    #State: `n` is a positive integer, `k` is an integer such that `1 <= k <= n`, `v` is the value returned by `func_2()` during the last iteration (`i = 1`), `cnt` is `0`, `l` is `n + 1`, and `i` is `n // k`.
    print('! -1', flush=True)
    #This is printed: ! -1
    func_2()
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_5` interacts with a hidden array of length `n` and an integer `k` such that `1 <= k <= n`. It prints queries to determine certain properties of the array and may print a result based on these queries. Regardless of the input values, the function does not return any value.

