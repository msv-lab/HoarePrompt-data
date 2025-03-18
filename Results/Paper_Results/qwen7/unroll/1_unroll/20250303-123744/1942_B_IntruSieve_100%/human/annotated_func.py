#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where -n ≤ a_i ≤ n; there is at least one valid permutation p for the given data; the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `minn` is greater than or equal to the maximum value in `a`, `mex` is a list containing elements that are increments of `minn` based on conditions in the loop, `used` is a dictionary marking integers that have been used according to the loop logic.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop prints each element in the list `mex` separated by a space.
    print()
    #This is printed: an empty line
#Overall this is what the function does:The function processes a list of integers `a` of length `n` and prints a sequence of integers `mex`. For each element in `a`, if the element is positive, `mex` contains the smallest non-negative integer not present in `a` up to that point. If the element is negative, `mex` contains the smallest non-negative integer that would make the element non-negative when subtracted from it. The function does not return any value but prints the sequence `mex` for each test case.

