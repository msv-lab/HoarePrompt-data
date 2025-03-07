#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should be `def construct_permutation(t, test_cases):` where `t` is an integer representing the number of test cases, and `test_cases` is a list of tuples, each containing an integer `n` and a list `a` of integers. For each test case, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of integers of length `n` where -n ≤ a_i ≤ n. The sum of `n` over all test cases does not exceed 2 · 10^5.
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
        
    #State: `mex` is a list of integers representing the MEX (Minimum EXcludant) values calculated for each element in `arr`. `minn` is the next positive integer that was not included in `mEX` during the loop execution. `maxx` is the maximum value that was appended to `mex` during the loop execution. The values of `t` and `test_cases` remain unchanged.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The values of `mex`, `minn`, `maxx`, `t`, and `test_cases` remain unchanged. The loop only prints the elements of `mex` in the same order they appear in the list, separated by spaces.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `construct_permutation` (as intended) should accept an integer `t` and a list of tuples `test_cases`. However, the provided code does not match this signature and instead reads input directly from the user. It processes a single list `arr` of integers, calculating a list `mex` of MEX (Minimum EXcludant) values based on the elements of `arr`. The function prints the MEX values separated by spaces and then prints an empty line. The function does not return any value. The state of the program after the function concludes includes the list `mex` containing the calculated MEX values, and the variables `minn` and `maxx` which were used in the calculation. The function does not modify the input variables `t` or `test_cases` as they are not used in the function.

