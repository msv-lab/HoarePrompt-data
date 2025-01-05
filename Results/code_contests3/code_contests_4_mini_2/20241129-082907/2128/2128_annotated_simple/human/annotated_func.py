#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ k < n ≤ 200000, k is a non-negative integer, and a is a list of n integers where each a_i is a non-negative integer such that 0 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 200000.
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
        
    #State of the program after the  for loop has been executed: `t` is greater than 0, `i` is `t - 1`, `n` is an integer greater than or equal to 2 for the last iteration, `k` is `n - 1`, `arr` is a list of integers sorted in descending order, and `ans` is the sum of the largest element in `arr` and the first `k` elements starting from `arr[1]`, printed for each iteration.
#Overall this is what the function does:The function accepts multiple test cases where each test case consists of two integers `n` and `k` followed by a list of `n` non-negative integers. It calculates the sum of the largest integer in the list and the next `k` largest integers (or `n-1` if `k` is greater than or equal to `n`) for each test case and prints the result. If `k` is adjusted to `n-1`, it ensures that the code does not add more elements than available in the list.

