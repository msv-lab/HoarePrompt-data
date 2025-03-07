#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each element a_i satisfies -n ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2 · 10^5. It is guaranteed that there is at least one valid permutation p for the given data.
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
        
    #State: `mex` is a list of integers constructed based on the rules specified in the loop, `minn` is the smallest integer that has not been used after the loop completes, and `used` is a dictionary containing all the integers that have been used during the loop.
    for itm in mex:
        print(itm, end=' ')
        
    #State: mex is a list of integers constructed based on the rules specified in the loop, minn is the smallest integer that has not been used after the loop completes, and used is a dictionary containing all the integers that have been used during the loop.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers for each test case. It then constructs and prints a list of integers based on specific rules involving the minimum unused non-negative integer and the absolute differences between the list elements and this minimum integer. The function outputs a space-separated list of integers for each test case, followed by an empty line.

