#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 1 ≤ k < n ≤ 2 ⋅ 10^5, k is a non-negative integer, and a is a list of n integers where each a_i is an integer such that 0 ≤ a_i ≤ 10^9. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 1000, `i` is equal to `t`, `k` is at least 0, `arr` is the sorted list of integers in descending order for the last iteration, and `ans` is the result of the last calculation based on the last `n`, `k`, and `arr`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, followed by a list of `n` integers. It sorts this list in descending order and calculates the sum of the largest integer and the next `k` largest integers, ensuring that `k` does not exceed `n - 1`. The function then prints the resulting sum for each test case. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. The function does not return any value; instead, it prints the results directly.

