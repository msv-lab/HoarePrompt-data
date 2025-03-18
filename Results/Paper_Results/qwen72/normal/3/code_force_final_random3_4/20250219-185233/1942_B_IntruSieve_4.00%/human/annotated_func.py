#State of the program right berfore the function call: The function `func_1` is expected to handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) representing the length of the permutation `p` and the array `a`, and an array `a` of length `n` with elements in the range (-n ≤ a_i ≤ n). The sum of `n` over all test cases does not exceed 2 · 10^5. It is guaranteed that at least one valid permutation `p` exists for the given `a`.
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
        
    #State: `minn` is the highest positive integer value encountered in `arr` + 1 (or 0 if no positive integers are in `arr`), `n` is the input integer, `arr` is the list of integers input by the user, `mex` is a list of integers where each element is either the value of `minn` before the iteration or the absolute difference between the corresponding element in `arr` and `minn`, `maxx` is the maximum value in `mex`, and `i` is `n - 1`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `minn` is the highest positive integer value encountered in `arr` + 1 (or 0 if no positive integers are in `arr`), `n` is the input integer, `arr` is the list of integers input by the user, `mex` is a list of integers that has been fully iterated, `i` is `n - 1`, and `itm` is the last element in `mex`.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `n` and an array `a` of length `n` from the user. It processes the array to generate a list `mex` of integers. For each element in `a`, if the element is positive, it appends the current value of `minn` to `mex` and increments `minn`. If the element is non-positive, it appends the absolute difference between the element and `minn` to `mex`. After processing all elements, it prints the elements of `mex` separated by spaces, followed by an empty line. The function does not return any value.

