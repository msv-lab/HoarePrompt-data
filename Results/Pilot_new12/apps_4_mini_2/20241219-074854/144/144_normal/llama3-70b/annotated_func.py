#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each element a[i] satisfies 1 ≤ a[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 100,000; `a` is a list of `n` positive integers where each element `a[i]` satisfies 1 ≤ `a[i]` ≤ 10^9; `arr` is a sorted list of `n` integers corresponding to `a`, and `mex` is the smallest positive integer that is not in `arr`, determined after processing all elements.
    print(mex)
#Overall this is what the function does:The function `func` accepts a positive integer `n` and a list `arr` of `n` positive integers, where each integer lies between 1 and 10^9. It processes the list by sorting it, then determines and prints the smallest positive integer that is not present in the sorted list. This integer is referred to as the 'minimum excluded value' (mex). The function correctly handles edge cases where the list may contain consecutive integers starting from 1, and it efficiently identifies the mex by breaking the loop as soon as it encounters a number greater than the current mex. The function does not return a value; instead, it outputs the mex directly. However, it does not include error handling for cases where input is invalid or outside the specified constraints.

