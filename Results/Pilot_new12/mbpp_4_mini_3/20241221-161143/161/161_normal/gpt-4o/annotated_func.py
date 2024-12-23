#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    if (n == 0) :
        return 2
        #The program returns the value 2
    else :
        if (n == 1) :
            return 1
            #The program returns 1
        else :
            a, b = 2, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
                
            #State of the program after the  for loop has been executed: `n` is a positive integer greater than 1; `a` is the Fibonacci-like value at index `n`, `b` is the Fibonacci-like value at index `n + 1`.
            return b
            #The program returns the Fibonacci-like value at index n + 1, denoted as b, where n is a positive integer greater than 1 and a is the Fibonacci-like value at index n.
#Overall this is what the function does:The function accepts a non-negative integer parameter `n`. It returns:
- The value 2 if `n` is 0.
- The value 1 if `n` is 1.
- For values of `n` greater than 1, it returns the Fibonacci-like value at index `n + 1`, calculated iteratively using the Fibonacci sequence logic, where the value at index `n` is represented by `a` and the value at index `n + 1` is represented by `b`. 

The function handles the base cases for `n = 0` and `n = 1` explicitly, ensuring correct outputs for these edge cases. In case of `n` being 2 or greater, it computes the next Fibonacci number starting from the first two Fibonacci-like numbers (2 and 1) and iteratively derives the subsequent values, hence returning the value for `b`. The function does not have guard clauses for negative integers, but is designed to operate effectively within the domain of non-negative integers only, as per the specified precondition.

