#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 1 ≤ k < n ≤ 2 ⋅ 10^5, and k is an integer; a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^{9}. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer input, `i` is equal to `t - 1`, `n` is an integer from input, `k` is at least 0, `arr` is a sorted list of integers in descending order, `ans` is the sum of the first element of `arr` and the first `k` elements of `arr` (excluding the first element) for each iteration, and the value of `ans` is printed for each iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case it reads two integers `n` and `k`, and a list of `n` integers. It sorts the list in descending order and computes the sum of the largest integer and the next `k` largest integers (up to `k` elements, ensuring that if `k` is greater than or equal to `n`, it only sums up to `n - 1`). The resulting sum is printed for each test case. The function does not accept parameters directly; it reads input from standard input.

