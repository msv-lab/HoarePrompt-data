#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies -n <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: `mex` is a list of `n` integers, `minn` is the next smallest non-negative integer not used in `mex`, and `maxx` is the maximum value in `mex`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `mex` is a list of `n` integers, `minn` is the next smallest non-negative integer not used in `mex`, and `maxx` is the maximum value in `mex`.
    print()
    #This is printed: (a blank line)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It then computes and prints a permutation `p` of `n` integers based on the values in `a`. Each integer in the permutation is derived from the values in `a` with specific rules involving non-negative integers and absolute differences. The function outputs the permutation for each test case, followed by a blank line.

