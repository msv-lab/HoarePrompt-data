#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5. h_i are integers such that 1 <= h_i <= 10^9 for 1 <= i <= n.**
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, 'n' is an input integer within the specified range, 'first' is assigned the first element of the list 'ar', 'dp' is updated with 'n' elements containing the minimum steps to reach each element, 'maxstack' and 'maxidx' are empty, 'minstack' contains the minimum element of 'ar', 'minidx' contains the index of the minimum element, 'ar' is a list with at least 1 element
    debug_print(dp)
    print(dp[n - 1])
#Overall this is what the function does:The function `func_1` reads an integer `n` from the user input, then calls another function `func_2` to get a list `ar`. It iterates through the list `ar` and calculates the minimum steps needed to reach each element while maintaining two stacks (`maxstack` and `minstack`) to keep track of maximum and minimum elements. The function aims to output the maximum possible height of a staircase that can be built using the given parameters `n` and `h_i`, where `n` is an integer between 2 and 3*10^5, and `h_i` are integers between 1 and 10^9.

#State of the program right berfore the function call: **
def func_2():
    return [int(x) for x in input().split()]
    #The program returns a list of integers converted from the input values obtained through splitting the input string
#Overall this is what the function does:The function func_2 does not accept any parameters and returns a list of integers converted from the input values obtained through splitting the input string. It accurately converts the input values to a list of integers as described in the annotations.

#State of the program right berfore the function call: **
def func_3(o):
    return [(int(x) + o) for x in input().split()]
    #The program returns a list of integers where each element is obtained by adding the integer value of each element in the input list (obtained by splitting the input string) with 'o'
#Overall this is what the function does:The function accepts a parameter `o` and returns a list of integers. Each element in the list is obtained by adding the integer value of each element in the input list (obtained by splitting the input string) with the value of `o`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5, and m is a list of n integers where each integer is between 1 and 10^9.**
def func_4(n, m):
    return [func_2() for _ in range(n)]
    #The program returns a list of n elements where each element is the result of calling func_2()
#Overall this is what the function does:The function func_4 accepts two parameters: an integer n where 2 <= n <= 3*10^5, and a list of n integers m where each integer is between 1 and 10^9. It then returns a list of n elements, where each element is the result of calling func_2().

#State of the program right berfore the function call: **
def func_5(f):
    return [func_5(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by calling function `func_5` with arguments `f` and the remaining dimensions in `dim`, repeated `dim[0]` times if `dim` is not empty. If `dim` is empty, it returns the result of calling function `f`.
#Overall this is what the function does:The function `func_5` accepts a function `f` and a variable number of dimensions in `dim`. It returns a list of values obtained by calling function `func_5` with arguments `f` and the remaining dimensions in `dim`, repeated `dim[0]` times if `dim` is not empty. If `dim` is empty, it returns the result of calling function `f`. The implementation recursively calls `func_5` with appropriate arguments based on the dimensions provided.

