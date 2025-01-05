#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `n` holds the input value, `ar` is assigned the result of `func_2()`, `first` is assigned the first element of `ar`, `dp` is a list of `n` elements where each element is the minimum number of moves to reach the element at index `i`, `maxstack` is empty, `maxidx` is empty, `minstack` contains the minimum value element from `ar`, `minidx` contains the index of the minimum value element in `ar`
    debug_print(dp)
    print(dp[n - 1])
#Overall this is what the function does:The function `func_1` reads an integer input `n`, calls `func_2` to get an array `ar`, and then performs a series of operations on the elements of `ar` to calculate the minimum number of moves required to reach each element. However, the function does not return any value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5. The list h contains n integers where each integer represents the height of a skyscraper, and each height value is between 1 and 10^9.**
def func_2():
    return [int(x) for x in input().split()]
    #The program returns a list of integers where each integer represents the height of a skyscraper
#Overall this is what the function does:The function func_2 does not accept any parameters and returns a list of integers representing the heights of skyscrapers extracted from the input list h. The code correctly reads input from the user and splits it into integers to form the list of skyscraper heights. The function does not have any edge cases or missing functionality as it accurately performs the described task.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5. h_i are integers such that 1 <= h_i <= 10^9 for 1 <= i <= n.**
def func_3(o):
    return [(int(x) + o) for x in input().split()]
    #The program returns a list of integers where each integer is the sum of the corresponding element in the input list after converting it to an integer and adding 'o'
#Overall this is what the function does:The function `func_3` accepts an integer `o` and reads a list of integers from input. It then converts each element in the list to an integer, adds `o` to each element, and returns a new list containing the sum of the elements. The function does not handle any errors that may occur during input reading or conversion, and it assumes the input list is valid.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 3*10^5. m is a list of n integers where each integer is in the range 1 <= h_i <= 10^9.**
def func_4(n, m):
    return [func_2() for _ in range(n)]
    #The program returns a list of n elements, where each element is the result of calling func_2()
#Overall this is what the function does:The function accepts an integer n and a list of n integers. It then returns a list of n elements where each element is the result of calling func_2().

#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 2 <= n <= 3 * 10^5.
- h_i (1 ≤ h_i ≤ 10^9) are integers representing the heights of the skyscrapers.
def func_5(f):
    return [func_5(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by calling function func_5 with arguments *dim[1:] for each element in the range of dim[0]. If dim is empty, it returns the result of calling function f().
#Overall this is what the function does:The function func_5 accepts a function f and returns a list of values obtained by calling function func_5 with arguments based on the elements in the range specified by the first element of dim. If dim is empty, it returns the result of calling function f(). The code provided does exactly as described in the annotations.

