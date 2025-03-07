#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: Output State: `minn` is the maximum value between the last updated `minn` and `maxx` + 1, `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 2 \cdot 10^5, `arr` is a list of integers obtained from splitting the input string and converting each element to an integer, `mex` is a list containing the values of `minn` for each positive element in `arr`, and `maxx` is the maximum value between the original `maxx` and the differences between elements in `arr` and `minn`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: The loop iterates over each value in the list `mex` and prints it, separated by spaces.
    print()
    #This is printed: a newline
#Overall this is what the function does:The function processes a list of integers `arr` and computes a list `mex` based on the positive elements in `arr`. It then prints each element of `mex` separated by spaces and followed by a newline. The function does not return any value but modifies and prints the `mex` list.

