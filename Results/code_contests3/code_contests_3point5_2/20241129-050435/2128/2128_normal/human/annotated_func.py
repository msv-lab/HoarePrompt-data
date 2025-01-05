#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ k < n ≤ 2 ⋅ 10^5. The list of initial water amounts a_i for each barrel contains n non-negative integers where 0 ≤ a_i ≤ 10^9. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.**
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
        
    #State of the program after the  for loop has been executed: The sum of the first `k+1` elements in `arr` is printed for each test case, where `k` is at least 1. The values of `n`, `k`, `arr`, `ans`, and other loop variables are updated accordingly for each iteration.
#Overall this is what the function does:The function `func` reads the number of test cases `t`, for each test case, it reads the number of barrels `n`, and a parameter `k`. It then reads the initial water amounts for each barrel, sorts them in descending order, and calculates the sum of the first `k+1` elements of the sorted array. If `k` is greater than or equal to `n`, it sets `k` to `n-1`. The function prints the sum for each test case. The function handles multiple test cases efficiently without returning any specific value.

