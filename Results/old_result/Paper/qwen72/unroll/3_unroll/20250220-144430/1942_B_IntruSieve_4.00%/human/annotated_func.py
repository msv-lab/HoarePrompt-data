#State of the program right berfore the function call: The function `func_1` is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 2 · 10^5) and an array a of length n with elements a_i (-n ≤ a_i ≤ n). The sum of n over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation p for the given data.
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
        
    #State: Output State: `n` is the same input integer, `arr` is the same list of integers, `mex` is a list of integers representing the appended values based on the conditions in the loop, `minn` is the final value of `minn` after all iterations, `maxx` is the final value of `maxx` after all iterations.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The values of `n`, `arr`, `minn`, and `maxx` remain unchanged. The loop prints each element of the `mex` list separated by a space.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `n` and an array `a` of length `n` from the input. It processes the array to generate a list `mex` of integers based on the values in `a`. For each positive element in `a`, it appends the current value of `minn` to `mex` and increments `minn`. If `minn` equals `maxx`, `minn` is set to `maxx + 1`. For each non-positive element in `a`, it appends the absolute difference between the element and `minn` to `mex`, and updates `maxx` if this difference exceeds the current `maxx`. Finally, it prints the elements of `mex` separated by spaces, followed by a newline. The function does not return any value.

