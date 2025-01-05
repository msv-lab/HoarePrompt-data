#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `t`, `n`, `k`, `ans`, `i`, `l` are positive integers; `ans` is the sum of the first `k` elements of the sorted array `arr`; `i` is equal to `t`; `k` is at least 1 and less than or equal to `n`; `l` is equal to `k`; the value of `ans` is printed for each iteration of the loop.
#Overall this is what the function does:The function reads input from the standard input, processes the data for each test case, calculates the sum of the first `k` elements of a sorted array `arr`, and prints the result. It handles cases where `k` is greater than or equal to `n` by adjusting `k` to `n - 1`. The function does not accept any parameters and returns a predefined output.

