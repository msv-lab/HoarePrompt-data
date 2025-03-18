#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the input consists of n integers a_1, a_2, \ldots, a_n where -n ≤ a_i ≤ n. It is guaranteed that there is at least one valid permutation p for the given data, and the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: `minn` is `maxx + 2` if `arr[i]` > 0 and `minn == maxx` for all `i` in the range of `n`, otherwise `minn` is the final value it reached during the loop execution. `mex` is a list containing all the values of `minn - 1` or `abs(arr[i] - minn)` for each iteration where `arr[i] > 0` and `minn == maxx`, otherwise it contains the appropriate value based on the conditions. `maxx` is the maximum of the absolute differences between `abs(arr[i])` and `minn` for each iteration. `i` is `n`. The variable `n` is the total number of elements in the list `arr`, and `arr` is the list of integers obtained from splitting the input string on spaces.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop will continue to execute as long as `mex` contains at least one element. Once `mex` becomes empty, the loop will terminate.
    print()
    #This is printed: \n
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`. It then calculates and prints a list `mex` which contains specific values based on the conditions provided in the code. Specifically, if `arr[i]` is greater than 0, `mex` includes `minn - 1`; otherwise, it includes `abs(arr[i] - minn)`. After processing all test cases, the function does not return any value but prints the results for each test case.

