#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    maxx = 0
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            minn += 1
            if minn == maxx:
                minn = maxx + 1
        else:
            mex.append(abs(arr[i] - minn))
            if abs(arr[i] - minn) > maxx:
                maxx = abs(arr[i] - minn)
        
    #State: `mex` is a list of `n` integers, `minn` is the final count of positive numbers in `arr` (adjusted by the rule that if `minn` equals `maxx`, it increments by 1), and `maxx` is the maximum absolute difference between any non-positive `arr[i]` and the current `minn`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: All elements of `mex` are printed, separated by spaces. `minn` and `maxx` remain unchanged.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It then computes and prints a list `mex` of `n` integers based on specific rules involving positive and non-positive numbers in the input list. Each test case results in a new line of output containing the elements of `mex` separated by spaces.

