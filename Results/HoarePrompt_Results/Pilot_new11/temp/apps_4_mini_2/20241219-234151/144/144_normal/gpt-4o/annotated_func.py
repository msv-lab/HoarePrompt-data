#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each element a[i] is such that 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `a` is a list of `n` positive integers sorted in ascending order, with `n` being within the range 1 ≤ `n` ≤ 100,000; `mex` is the smallest positive integer not present in list `a`, which is in the range 1 to `n + 1`. If all elements of `a` are less than or equal to `n`, then `mex` can reach up to `n + 1`. If the loop does not execute, `mex` remains 1.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n`, which denotes the number of elements in a list `a` of `n` positive integers. It reads these integers from input, sorts the list `a`, and determines the smallest positive integer (`mex`) that is not present in the list. The final result is printed, which represents the value of `mex`. This can be any integer in the range from 1 to `n + 1`, considering that all elements of `a` are positive integers and the function checks each integer sequentially starting from 1 against the sorted list `a`. In the case where all integers from 1 to `n` are present in the list, the function will return `n + 1`. Additionally, if the input list is empty or consists of integers outside the specified range, this could lead to unexpected results, but such situations are constrained by the input conditions specified at the start of the function. Therefore, any violation of these constraints is extraneous to the function's defined behavior.

