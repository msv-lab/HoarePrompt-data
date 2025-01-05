#State of the program right berfore the function call: The function will receive multiple test cases, where each test case consists of an integer n (1 ≤ n ≤ 200,000), an integer k (1 ≤ k < n), and a list of n non-negative integers representing the amounts of water in the barrels (0 ≤ a_i ≤ 10^9). The total number of barrels across all test cases will not exceed 200,000.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `i` is `t - 1`, `n` is the number of barrels in the last test case, `k` is the value assigned in the last test case (which could be either `n-1` or the input value), `arr` is a sorted list of barrel amounts for the last test case, and `ans` is the sum of the first element of `arr` and the next `k` elements in `arr`.
#Overall this is what the function does:The function processes multiple test cases where each test case consists of an integer `n`, an integer `k`, and a list of `n` non-negative integers representing amounts of water in barrels. It calculates the maximum possible sum of water by taking the largest barrel and the next `k` largest barrels, returning this sum for each test case. If `k` is greater than or equal to `n`, it adjusts `k` to `n-1` to avoid exceeding the list's index.

