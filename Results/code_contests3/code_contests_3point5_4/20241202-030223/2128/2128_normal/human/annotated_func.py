#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 1 ≤ k < n ≤ 2 ⋅ 10^5. The list of initial water amounts a contains n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^9.**
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
        
    #State of the program after the  for loop has been executed: `t` is an input integer representing the number of test cases, `i` is `t-1`, `n`, `k`, `arr` is a list of integers sorted in descending order, `ans` is the sum of the first `k` elements in `arr`, `k` is less than `n`, `l` is equal to `k+1` for the last iteration. `ans` is printed for all `t` test cases.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads integers `n` and `k`, followed by a list of `n` integers. It sorts the list in descending order, calculates the sum of the first `k` elements, and prints the result. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. The function executes this process for all `t` test cases.

