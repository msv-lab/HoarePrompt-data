#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the integer value read from the input, where 1 ≤ n ≤ 2 · 10^5; `arr` is a list of `n` integers where each `arr_i` satisfies -n ≤ `arr_i` ≤ n; `mex` is a list of `n` integers computed based on the loop conditions; `minn` is the smallest non-negative integer not used in `mex`; `used` is a dictionary of all unique values in `mex`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: the elements of `mex` printed in a single line, separated by spaces.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It computes a list `mex` based on the values in `arr` and prints the elements of `mex` in a single line, separated by spaces. Each element in `mex` is determined by the smallest non-negative integer not used in `mex` up to that point or the absolute difference between the current element in `arr` and the smallest non-negative integer not used, depending on whether the current element is positive or not. After processing the list, it prints an empty line.

