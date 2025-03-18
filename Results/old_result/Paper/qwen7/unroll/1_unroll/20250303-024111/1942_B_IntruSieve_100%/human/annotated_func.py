#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where -n ≤ a_i ≤ n for all i.
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
        
    #State: Output State: `minn` is 10001 (since `t` is a positive integer such that 1 ≤ t ≤ 10^4, and `minn` is incremented until it is greater than `t`), `mex` is a list of integers where each element is either `minn` or `abs(arr[i] - minn)` depending on the value of `arr[i]`, and `used` is a dictionary with keys ranging from 0 to `minn-1` where each key is set to `True`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: minn is 10001, mex is a list of integers where each element is either 10001 or abs(arr[i] - 10001) depending on the value of arr[i], and used is a dictionary with keys ranging from 0 to 10000 where each key is set to True. The loop prints each element of the mex list separated by a space.
    print()
    #This is printed: \n
#Overall this is what the function does:The function processes a list of integers `a` of length `n`. It calculates a modified exclusive maximum (mex) for each element in the list based on whether the element is positive or negative. If the element is positive, it appends the current minimum unused non-negative integer (`minn`). If the element is negative, it appends the absolute difference between the element and the current minimum unused non-negative integer. The function then prints these mex values for each element in the list, separated by spaces. After processing, the function sets `minn` to 10001 and ensures that all integers from 0 to `minn-1` are marked as used in a dictionary.

