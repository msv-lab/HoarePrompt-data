#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n for all i, and there exists at least one valid permutation p that satisfies the given conditions.
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
        
    #State: Output State: `minn` is greater than or equal to the maximum value in `arr`, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `mex` is a list containing differences or `minn` based on conditions, `maxx` is the maximum difference found between elements in `arr` and `minn`.
    for itm in mex:
        print(itm, end=' ')
        
    #State: `minn` is greater than or equal to the maximum value in `arr`, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `mex` is a list containing the differences or `minn` based on conditions, `maxx` is the maximum difference found between elements in `arr` and `minn`, the loop prints each element of `mex` separated by a space.
    print()
    #This is printed: minn - a1 minn - a2 ... minn - an
#Overall this is what the function does:The function processes a list of integers `arr` and calculates a list `mex` based on specific conditions. It then prints each element of `mex` separated by a space. After processing, `minn` is updated to be greater than or equal to the maximum value in `arr`, while `t`, `n`, `arr`, and `maxx` remain unchanged. The function does not return any value but modifies and prints the `mex` list.

