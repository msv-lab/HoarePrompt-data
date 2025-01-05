#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5, and h_i are integers such that 1 <= h_i <= 10^9 for 1 <= i <= n.**
def func_1():
    n = int(input())
    ar = func_2()
    first = ar[0]
    dp = [0] * n
    maxstack = [first]
    maxidx = [0]
    minstack = [first]
    minidx = [0]
    for (i, x) in enumerate(ar):
        if i == 0:
            continue
        
        dp[i] = dp[i - 1] + 1
        
        while minstack and minstack[-1] > x:
            minstack.pop()
            minidx.pop()
        
        while maxstack and maxstack[-1] < x:
            maxstack.pop()
            maxidx.pop()
        
        if minidx:
            dp[i] = min(dp[i], dp[minidx[-1]] + 1)
        
        if maxidx:
            dp[i] = min(dp[i], dp[maxidx[-1]] + 1)
        
        if minstack and minstack[-1] == x:
            minstack.pop()
            minidx.pop()
        
        if maxstack and maxstack[-1] == x:
            maxstack.pop()
            maxidx.pop()
        
        minstack.append(x)
        
        minidx.append(i)
        
        maxstack.append(x)
        
        maxidx.append(i)
        
    #State of the program after the  for loop has been executed: At the end of the loop, `n` is an integer where 2 <= n <= 3*10^5; `first` is the first element of the list `ar`; `dp` is a list of n integers calculated based on the conditions within the loop; `ar` is a list with at least 1 element; `i` is n-1; `x` is the last element in the list; `maxstack` and `maxidx` contain the maximum element and its index respectively; `minstack` and `minidx` contain the minimum element and its index respectively.
    debug_print(dp)
    print(dp[n - 1])
#Overall this is what the function does:The function `func_1` reads an integer `n` from input and then calls `func_2` to get a list `ar`. It initializes various lists and variables based on the input. It then iterates through the elements of `ar`, updating a dynamic programming list `dp` based on certain conditions. Finally, it prints the last element of `dp` after the loop ends. The function internally handles the constraints and operations based on the input, but the exact nature of these operations based on the logic inside the loop is not explicitly described in the annotations.

#State of the program right berfore the function call: **
def func_2():
    return [int(x) for x in input().split()]
    #The program returns a list of integers converted from the input values provided by the user
#Overall this is what the function does:The function `func_2` prompts the user to input values, converts those input values to integers, and returns a list of integers. This function does not accept any parameters.

#State of the program right berfore the function call: **
def func_3(o):
    return [(int(x) + o) for x in input().split()]
    #The program returns a list of integers where each element is obtained by adding the integer value of each element separated by a space in the input to the value of variable 'o'
#Overall this is what the function does:The function func_3 accepts a parameter `o` and returns a list of integers where each element is obtained by adding the integer value of each element separated by a space in the input to the value of variable `o`. The function reads input from the user and splits it by space, then converts each element to an integer before adding `o` to it.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5, and m is a list of n integers where each integer is between 1 and 10^9.**
def func_4(n, m):
    return [func_2() for _ in range(n)]
    #The program returns a list of n elements, where each element is the result of calling func_2()
#Overall this is what the function does:The function func_4 accepts an integer n and a list of n integers m. It then returns a list of n elements, where each element is the result of calling func_2().

#State of the program right berfore the function call: **
def func_5(f):
    return [func_5(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by applying 'func_5' to the arguments '*dim[1:]' for each element in the range of 'dim[0]'. If 'dim' is empty, the program returns the result of calling function 'f'.
#Overall this is what the function does:The function func_5 accepts a parameter `f` and returns a list of values obtained by applying 'func_5' to the arguments '*dim[1:]' for each element in the range of 'dim[0]'. If 'dim' is empty, the program returns the result of calling function 'f'. However, there seems to be a missing definition or initialization of the variable `dim` in the code, which could potentially lead to errors or unexpected behavior.

