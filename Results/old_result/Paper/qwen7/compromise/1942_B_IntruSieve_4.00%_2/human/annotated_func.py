#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the array a is a list of n integers where -n ≤ a_i ≤ n.
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
        
    #State: Output State: `minn` is greater than or equal to the maximum value in `arr`, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `mex` is a list containing values from `minn` up to the maximum value in `arr` and differences calculated based on conditions, `maxx` is the maximum difference found between elements in `arr` and `minn`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `itm` takes on each value in `mex` in order, starting from `minn` up to the maximum value in `arr`, with `minn`, `t`, `n`, `arr`, and `mex` remaining unchanged, and `maxx` remaining unchanged.
    print()
    #This is printed: None
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a positive integer `n` and an array `a` of `n` integers. It calculates a list `mex` which contains values starting from `minn` up to the maximum value in `arr`, along with some differences based on conditions. Finally, it prints each value in `mex` in order, followed by a newline. The function does not return any value but modifies a local list `mex` and prints the results.

