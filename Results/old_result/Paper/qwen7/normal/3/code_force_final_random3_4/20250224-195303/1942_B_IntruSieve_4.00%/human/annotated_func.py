#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: After all iterations, `mex` will be a list containing all the values of `minn` updated during each iteration where `arr[i] > 0`, and the absolute differences between `arr[i]` and `minn` when `arr[i] <= 0`. The final value of `minn` will be the last updated value of `minn` after the loop completes, and `maxx` will be the maximum value among all the absolute differences calculated during the loop.
    for itm in mex:
        print(itm, end=' ')
        
    #State: After the loop executes all the iterations, `mex` is a list containing all the values of `minn` updated during each iteration where `arr[i] > 0`, and the absolute differences between `arr[i]` and `minn` when `arr[i] <= 0`. The final value of `itm` is the last element of `mex`, and `maxx` is the maximum value among all the absolute differences calculated during the loop.
    print()
    #This is printed: Output:
#Overall this is what the function does:The function processes a list of integers `arr` and calculates a list `mex` based on the values of `minn` and the absolute differences between elements of `arr` and `minn`. It then prints each element of `mex` followed by a space, and finally prints a newline character. The function does not return any value but modifies and prints the list `mex` based on the input list `arr`.

