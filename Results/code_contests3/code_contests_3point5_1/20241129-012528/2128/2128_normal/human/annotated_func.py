#State of the program right berfore the function call: **Precondition**: **t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 1 ≤ k < n ≤ 2 ⋅ 10^5. The list of initial amounts of water a_i for each test case contains n integers where 0 ≤ a_i ≤ 10^9.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `t` is greater than or equal to 0, `n` and `k` have assigned values, `arr` is a list of integers sorted in descending order, and `ans` is the sum of the largest `k` elements in the list, printed for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the standard input. Then, for each test case (denoted by `i` from 0 to `t`), it reads integers `n` and `k`. It reads a list of integers `arr`, sorts it in descending order, and calculates the sum of the largest `k` elements in the list. If `k` is greater than or equal to `n`, it sets `k` to `n - 1`. The function then prints the sum `ans` for each test case. The function does not return any value.

