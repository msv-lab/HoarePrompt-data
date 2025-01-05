#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 1000) representing the number of test cases; for each test case, n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5) representing the number of barrels and k is an integer representing the number of pourings; a is a list of n integers (0 ≤ a_i ≤ 10^{9}) representing the initial amount of water in each barrel, where the total number of barrels across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `i` is at least `t - 1`, `n` and `k` are values obtained from input, `arr` is a list of integers sorted in descending order, `ans` is the sum of the first `min(k + 1, n)` elements of `arr`, and the final value of `ans` is printed for each test case.
#Overall this is what the function does:The function accepts multiple test cases, where for each test case it reads two integers `n` (number of barrels) and `k` (number of pourings), followed by a list of integers representing the initial amount of water in each barrel. It then calculates and prints the sum of the largest amounts of water in the top `min(k + 1, n)` barrels across all test cases. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. The function does not return any value; it only prints the results for each test case.

