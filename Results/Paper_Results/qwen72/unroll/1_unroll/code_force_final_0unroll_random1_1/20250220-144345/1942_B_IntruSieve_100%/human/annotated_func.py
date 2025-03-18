#State of the program right berfore the function call: The function `func_1` is expected to handle multiple test cases. For each test case, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of `n` integers where -n ≤ a_i ≤ n. The sum of `n` over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation `p` for each given `a`.
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
        
    #State: `mex` is a list of integers representing the MEX (Minimum EXcludant) values computed for each element in `arr`. `minn` is the smallest non-negative integer not present in `used`. `used` is a dictionary containing all the integers that have been used in the MEX computation.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop prints each integer in the `mex` list separated by a space. The values of `mex`, `minn`, and `used` remain unchanged.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers `arr` from the user. It computes the MEX (Minimum EXcludant) values for each element in `arr` and stores these values in a list `mex`. The MEX value for each element is the smallest non-negative integer that has not been used in the MEX computation so far. The function then prints each MEX value in the `mex` list, separated by a space, followed by an empty line. The function does not return any value; it only performs I/O operations and modifies local variables.

