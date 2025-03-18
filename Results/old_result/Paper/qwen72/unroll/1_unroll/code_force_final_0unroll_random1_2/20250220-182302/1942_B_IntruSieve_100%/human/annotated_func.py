#State of the program right berfore the function call: The function `func_1` is expected to handle multiple test cases. For each test case, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of integers of length `n` where -n ≤ a_i ≤ n. The sum of `n` over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation `p` for each test case.
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
        
    #State: Output State: `mex` is a list of integers where each element is either the current `minn` value (if `arr[i]` is positive) or the absolute difference between `arr[i]` and `minn` (if `arr[i]` is non-positive). `minn` is the smallest non-negative integer that has not been added to the `used` dictionary. `used` is a dictionary containing all the integers that have been added to `mex` as keys, with their values set to `True`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The elements of `mex` are printed in the order they appear in the list, separated by spaces. The values of `minn` and `used` remain unchanged.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the user. It processes `arr` to generate a list `mex` of integers, where each element is determined based on the current smallest non-negative integer (`minn`) that has not been used and the value of `arr[i]`. If `arr[i]` is positive, the current `minn` is added to `mex` and marked as used. If `arr[i]` is non-positive, the absolute difference between `arr[i]` and `minn` is added to `mex` and marked as used. The function then prints the elements of `mex` separated by spaces, followed by a newline. The function does not return any value.

