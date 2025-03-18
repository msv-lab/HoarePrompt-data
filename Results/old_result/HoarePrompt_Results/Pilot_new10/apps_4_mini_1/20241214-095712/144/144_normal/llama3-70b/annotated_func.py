#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an input positive integer such that 1 ≤ `n` ≤ 100,000; `a` is a sorted list of `n` positive integers; `mex` is the smallest positive integer that is not in `arr`; `arr` is a sorted list of positive integers of length `n`. If the loop executes fully, it means that `mex` has been increased for every number in `arr` up to the maximum value of the elements in the array; if the loop doesn't execute due to the first element being greater than 1, `mex` remains 1.
    print(mex)
#Overall this is what the function does:The function reads a positive integer `n` and a list of `n` positive integers, then computes the smallest positive integer that is not present in the list (referred to as the "minimum excluded value", or mex). It handles cases where the list is empty or all numbers in the list are greater than 1. The function outputs this smallest missing positive integer but does not return any value.

