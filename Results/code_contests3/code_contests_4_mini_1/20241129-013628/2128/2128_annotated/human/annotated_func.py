#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ k < n ≤ 200000, k is a non-negative integer, and a is a list of n integers where each element a_i satisfies 0 ≤ a_i ≤ 10^9. The total number of barrels across all test cases does not exceed 200000.
def func():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n, k = map(int, sys.stdin.readline().split(' '))
        
        arr = list(map(int, sys.stdin.readline().split()))
        
        arr = sorted(arr, reverse=True)
        
        ans = arr[0]
        
        if k >= n:
            k = n - 1
        
        for l in range(1, k + 1):
            ans += arr[l]
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 1000; `i` is `t - 1`; `n` is the last input value read; `k` is the last input value read adjusted to at most `n - 1`; `arr` is the sorted list of integers in descending order from the last input; `ans` is the sum of the first `min(k, n - 1)` elements of `arr` if `n > 1`, or the first element of `arr` if `n = 1.
#Overall this is what the function does:The function accepts multiple test cases, where each test case consists of an integer `n` (the number of elements in a list) and an integer `k` (the number of elements to sum starting from the highest). It reads a list of `n` integers, sorts them in descending order, and computes the sum of the largest `k + 1` elements. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. The function prints the computed sum for each test case. It also handles the edge case where if `n` is 1, it simply returns the first (and only) element. However, it does not handle cases where `k` is negative or the input values are outside of the specified constraints, which could lead to unexpected behavior.

