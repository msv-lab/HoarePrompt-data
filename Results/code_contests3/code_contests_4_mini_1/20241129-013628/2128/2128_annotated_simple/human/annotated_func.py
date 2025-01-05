#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 1 ≤ k < n ≤ 2 ⋅ 10^5, k is an integer such that 1 ≤ k < n, and a is a list of n integers where each a_i is a non-negative integer such that 0 ≤ a_i ≤ 10^9. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer greater than 0, `i` is `t - 1`, `n` is an integer greater than 0, `k` is at least 0, `arr` is a sorted list of integers in descending order from the last iteration, `ans` is the sum of the largest element of `arr` and all elements from `arr[1]` to `arr[k]` from the last iteration, and the value of `ans` has been printed for each iteration.
#Overall this is what the function does:The function reads multiple test cases and for each test case, it accepts two integers `n` and `k`, followed by a list of `n` non-negative integers. It calculates the sum of the largest integer in the list and the next `k` largest integers. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. The function outputs the calculated sum for each test case. However, it does not handle cases where `k` is negative or greater than `n`, nor does it validate the input format for the list of integers.

