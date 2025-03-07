#State of the program right berfore the function call: The function `func_1` is expected to handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) representing the length of the permutation `p` and the array `a`, and an array `a` of length `n` with elements in the range -n to n (-n ≤ a_i ≤ n). The sum of `n` over all test cases does not exceed 2 · 10^5, and there is at least one valid permutation `p` for each test case.
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
        
    #State: The `mex` list is populated with values based on the conditions in the loop. `minn` is updated to the next integer that was not included in the `mex` list due to positive elements in `arr`. `maxx` is updated to the maximum value encountered in the `mex` list due to negative elements in `arr`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The `mex` list is printed with its elements separated by spaces. The values of `minn` and `maxx` remain unchanged.
    print()
    #This is printed: (a newline character)
#Overall this is what the function does:The function `func_1` reads an integer `n` and an array `a` of length `n` from the input. It processes the array `a` to generate a list `mex` of length `n` based on the values in `a`. For each element in `a`, if the element is positive, it appends the current value of `minn` to `mex` and increments `minn`. If the element is negative, it appends the absolute difference between the element and `minn` to `mex` and updates `maxx` if this difference exceeds the current `maxx`. Finally, it prints the elements of `mex` separated by spaces, followed by a newline. The function does not return any value.

