#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 1000), n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5), k is an integer (1 ≤ k < n), and a is a list of n integers (0 ≤ a_i ≤ 10^9) representing the initial amounts of water in the barrels. The total number of barrels across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `n`, `k`, `a` remain unchanged; `ans` is the sum of the first `min(k + 1, n)` largest elements from the input array for each iteration of the loop, printed `t` times.
#Overall this is what the function does:The function processes multiple test cases where for each test case, it reads integers `n` (number of barrels) and `k` (number of barrels to consider) and a list of integers representing the initial amounts of water in the barrels. It calculates and prints the sum of the largest `k + 1` amounts of water from the barrels for each test case. If `k` is greater than or equal to `n`, it sums all the water amounts. The function does not directly accept parameters as input but reads them from standard input. It handles up to 1000 test cases and ensures that the total number of barrels across all test cases does not exceed 200,000.

