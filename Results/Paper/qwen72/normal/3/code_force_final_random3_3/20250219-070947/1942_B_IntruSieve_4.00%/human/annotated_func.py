#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should be `def construct_permutation(t, test_cases):`, where `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), and `test_cases` is a list of tuples, each containing an integer `n` (1 ≤ n ≤ 2 · 10^5) and a list `a` of `n` integers (-n ≤ a_i ≤ n). The sum of `n` over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `n` is the same as the initial `n`, `i` is `n-1`, `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples, each containing an integer `n` (1 ≤ n ≤ 2 · 10^5) and a list `a` of `n` integers (-n ≤ a_i ≤ n), `arr` is the same list of integers input by the user, `mex` is a list of integers that has been constructed based on the conditions in the loop, `minn` is the next integer that has not been added to `mex` or is 0 if all positive integers up to `maxx` have been used, and `maxx` is the maximum value in the `mex` list.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `n` is the same as the initial `n`, `i` is `n-1`, `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4), `test_cases` is a list of tuples, each containing an integer `n` (1 ≤ n ≤ 2 · 10^5) and a list `a` of `n` integers (-n ≤ a_i ≤ n), `arr` is the same list of integers input by the user, `mex` is a list of integers that has been fully printed, `itm` is the last element in `mex`, `minn` is the next integer that has not been added to `mex` or is 0 if all positive integers up to `maxx` have been used, and `maxx` is the maximum value in the `mex` list.
    print()
    #This is printed: (a newline character)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers from the user. It then constructs a new list `mex` based on the conditions in the loop. For each element in the input list `arr`, if the element is positive, the smallest non-negative integer not yet in `mex` is added to `mex`. If the element is non-positive, the absolute difference between the element and the smallest non-negative integer not yet in `mex` is added to `mex`. After constructing the `mex` list, it prints each element of `mex` separated by spaces, followed by a newline character. The function does not return any value. The final state of the program includes the original `n` and `arr`, the constructed `mex` list, and the updated values of `minn` and `maxx`.

