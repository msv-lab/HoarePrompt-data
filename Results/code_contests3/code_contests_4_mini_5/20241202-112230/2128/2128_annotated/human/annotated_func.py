#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ k < n ≤ 2 ⋅ 10^5, k is a non-negative integer, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^{9}.
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
        
    #State of the program after the  for loop has been executed: `t` is the original input value (>= 0), `i` is `t - 1` if `t > 0`, `n` is the last input value (>= 1), `k` is the last input value (>= 0 and <= n - 1), `arr` is the last sorted list of integers in descending order, `ans` is the sum of the first element of `arr` and the elements from `arr[1]` to `arr[k]` for the last iteration.
#Overall this is what the function does:The function reads an integer `t` which indicates the number of test cases. For each test case, it reads two integers `n` and `k`, followed by a list of `n` integers. The function sorts the list in descending order and calculates the sum of the largest element and the next `k` largest elements, ensuring that `k` does not exceed `n-1`. The computed sum is then printed for each test case. If `k` is greater than or equal to `n`, it is adjusted to `n-1`. The function does not return any values but outputs the results directly.

