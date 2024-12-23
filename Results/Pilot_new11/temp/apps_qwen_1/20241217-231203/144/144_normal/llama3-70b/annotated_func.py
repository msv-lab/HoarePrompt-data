#State of the program right berfore the function call: The function does not take any input parameters. The input values (n and the array a) are read from standard input as specified in the problem description.
def func():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mex = 1
    for num in arr:
        if num == mex:
            mex += 1
        elif num > mex:
            break
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `arr` is a sorted list of integers, and `mex` is the smallest non-negative integer not present in `arr`.
    print(mex)
#Overall this is what the function does:The function reads two inputs from standard input: an integer `n` and an array `a` of `n` integers. It then sorts the array and calculates the smallest non-negative integer that is not present in the array. The function outputs this integer to standard output. The function does not return any value. Potential edge cases include when the array contains all integers from 0 to `n-1`, or when the array is empty. In such cases, the function correctly outputs `n` and `0` respectively.

