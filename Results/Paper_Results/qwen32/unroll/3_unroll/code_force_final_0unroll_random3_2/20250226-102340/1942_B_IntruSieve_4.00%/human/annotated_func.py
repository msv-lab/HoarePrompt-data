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
        
    #State: `mex` is a list of integers as per the described logic, `minn` is the final value of `minn` after the loop, and `maxx` is the maximum value of `abs(arr[i] - minn)` encountered for non-positive `arr[i]` values.
    for itm in mex:
        print(itm, end=' ')
        
    #State: mex is the same list of integers, minn is the final value of minn after the loop, and maxx is the maximum value of abs(arr[i] - minn) encountered for non-positive arr[i] values.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It then computes and prints a specific permutation of the list `a` based on certain rules. For each positive element in the list, it assigns the current minimum non-negative integer not yet used, and for each non-positive element, it computes the absolute difference between the element and the current minimum non-negative integer, updating the maximum value encountered. The function prints the resulting permutation for the given list `a`.

