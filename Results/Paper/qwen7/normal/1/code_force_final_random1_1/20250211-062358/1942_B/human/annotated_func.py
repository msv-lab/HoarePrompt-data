#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        res = [None] * n
        
        mex = n
        
        for i in range(len(ar) - 1, -1, -1):
            res[i] = mex - ar[i]
            if mex > mex - ar[i]:
                mex = mex - ar[i]
        
        print(' '.join(str(x) for x in res))
        
    #State: Output State: After the loop executes all iterations, `i` is `-1`, `mex` remains unchanged (it could be any non-negative integer depending on the input but will be the smallest non-negative integer not present in the adjusted list `ar`), `res` is a list of length `n` where each element is calculated as `mex - ar[i]` for each index `i` from `len(ar) - 1` to `0`, and `ar` remains unchanged.
    #
    #Explanation: After the loop completes all its iterations, `i` will become `-1` because the loop decrements `i` starting from `len(ar) - 1` until it reaches `-1`. The value of `mex` remains unchanged throughout the loop as it is only modified within the if condition which does not alter `mex` if the condition is false. The list `res` is filled such that for each index `i`, `res[i]` equals `mex - ar[i]`. The list `ar` remains unaltered as it is not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( n \), a list \( a \) of \( n \) integers, and calculates a new list \( res \) based on the values in \( a \). Specifically, for each index \( i \) from \( n-1 \) to \( 0 \), it sets \( res[i] \) to \( mex - a[i] \), where \( mex \) is the smallest non-negative integer not present in the adjusted list \( a \). The function then prints the elements of \( res \) separated by spaces. The original list \( a \) remains unchanged.

