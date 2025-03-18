#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n integers where -n ≤ a_i ≤ n for all 1 ≤ i ≤ n.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    used = {}
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            used[minn] = True
            while minn in used:
                minn += 1
        else:
            mex.append(abs(arr[i] - minn))
            used[abs(arr[i] - minn)] = True
        
    #State: `minn` is greater than or equal to the maximum value in `arr`, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `mex` is a list containing non-negative integers, `used` is a dictionary with keys as integers and values as booleans.
    for itm in mex:
        print(itm, end=' ')
        
    #State: minn is greater than or equal to the maximum value in arr, t remains unchanged, n remains unchanged, arr remains unchanged, mex is iterated over and printed, used remains unchanged.
    print()
    #This is printed: an empty line
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It calculates and prints a list `mex` which contains non-negative integers. Each element in `mex` represents the smallest non-negative integer not present in the original list `a`. The function does not return any value but prints the elements of `mex` one by one.

