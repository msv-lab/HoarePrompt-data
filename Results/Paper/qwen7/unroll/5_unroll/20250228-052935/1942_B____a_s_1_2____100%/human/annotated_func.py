#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n integers such that -n ≤ a_i ≤ n, and there exists at least one valid permutation p that satisfies the given conditions.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: Output State: t is an integer between 1 and 10^4 inclusive. For each iteration of the loop, n is an integer, a is a list of n integers, and p is a list of n integers where each element p[i] is calculated as mex - a[i] with mex being the minimum value between the current mex and (mex - a[i]) as the loop iterates backwards from n-1 to 0. After all iterations, p contains the final values computed for each input case.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (number of test cases), a positive integer \( n \) (size of the list), and a list of \( n \) integers \( a \). For each test case, it calculates a permutation \( p \) of length \( n \) such that each element \( p[i] \) is equal to \( \text{mex} - a[i] \), where \( \text{mex} \) is the smallest non-negative integer not present in the list \( p \) so far. The function then prints the permutation \( p \) for each test case.

