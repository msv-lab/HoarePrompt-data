#State of the program right berfore the function call: The function should accept two parameters: the number of test cases t (1 ≤ t ≤ 10^4) and for each test case, an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (-n ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for each test case.
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
        
    #State: `n` is the same input integer, `arr` is the same list of integers input by the user, `mex` is a list of integers where each element is either the smallest non-negative integer not in `used` if `arr[i] > 0`, or the absolute difference between `arr[i]` and the smallest non-negative integer not in `used` if `arr[i] <= 0`, `minn` is the smallest non-negative integer not in `used` after processing all elements in `arr`, and `used` is a dictionary containing all integers that have been added to `mex` as keys, with their values set to `True`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop prints each element in the `mex` list separated by a space. The values of `n`, `arr`, `minn`, and `used` remain unchanged.
    print()
    #This is printed: (a newline character)
#Overall this is what the function does:The function `func_1` processes a single test case. It accepts an integer `n` and a list of `n` integers `arr` from user input. It generates a list `mex` where each element is determined based on the current smallest non-negative integer not found in the `used` dictionary. If the current element in `arr` is positive, the smallest non-negative integer not in `used` is added to `mex`. If the current element is non-positive, the absolute difference between the current element and the smallest non-negative integer not in `used` is added to `mex`. After processing all elements, the function prints each element in `mex` separated by a space, followed by a newline. The function does not return any value, and the final state of the program includes the unchanged values of `n` and `arr`, the `mex` list that has been printed, and the `used` dictionary that contains all integers added to `mex` as keys with their values set to `True`.

