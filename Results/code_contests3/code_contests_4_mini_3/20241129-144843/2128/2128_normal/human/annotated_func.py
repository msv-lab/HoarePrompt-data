#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, each test case consists of two integers n and k (1 ≤ k < n ≤ 2 ⋅ 10^5), and a list of n integers a_i (0 ≤ a_i ≤ 10^9) representing the initial amounts of water in the barrels, with the total sum of n across all test cases not exceeding 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is the last integer read, `k` is the last value of `k` computed, `arr` is the sorted list of integers from the last input, and `ans` is the sum of the first `n` elements of `arr` plus the sum of the first `k` elements of `arr` starting from index 1.
#Overall this is what the function does:The function accepts an integer `t`, representing the number of test cases. For each test case, it reads two integers `n` and `k`, followed by a list of `n` integers representing the amounts of water in barrels. It sorts this list in descending order, then calculates the sum of the largest element and the next `k` largest elements (up to the first `k` elements in the sorted list). It prints this sum for each test case. If `k` is greater than or equal to `n`, it uses `n - 1` instead of `k` to ensure valid indexing. The function does not return values but prints the results directly.

