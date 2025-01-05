#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000) representing the number of test cases; for each test case, n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5) representing the number of barrels, k is an integer representing the number of pourings allowed; a is a list of n integers (0 ≤ a_i ≤ 10^9) representing the initial amount of water in each barrel. The total sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is greater than 0, `i` is less than `t`, `ans` is the largest element in `arr` plus the sum of the first `k` elements in `arr` starting from index 1 (or up to `n-1` if `k` is greater than or equal to `n`), `n` is greater than 0, `k` is at least 0, and `arr` is a sorted list of integers.
#Overall this is what the function does:The function accepts multiple test cases where each test case specifies the number of barrels and the number of pourings allowed. It reads the initial amounts of water in each barrel, sorts them in descending order, and calculates the total amount of water by adding the largest amount and the amounts of the next `k` largest barrels (or up to `n-1` barrels if `k` is greater than or equal to `n`). The function prints the total amount of water for each test case. It does not return any values; it only prints the results.

