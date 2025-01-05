#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000) representing the number of test cases; for each test case, n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5) representing the number of barrels, and k is an integer representing the number of pourings you can make; a is a list of n non-negative integers (0 ≤ a_i ≤ 10^9) representing the initial amount of water in each barrel. The total sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `ans` is the sum of the first element of `arr` and the first `k` elements of `arr` for each test case, `arr` is a sorted list of integers in descending order for each test case, `k` is at least 0 for each test case, and `t` is the number of test cases.
#Overall this is what the function does:The function accepts multiple test cases where each test case consists of a positive integer `n` (the number of barrels) and `k` (the number of pourings) along with a list of integers representing the initial water amounts in each barrel. For each test case, it calculates the sum of the largest amount of water in the barrels and the next `k` largest amounts. If `k` is greater than or equal to `n`, it adjusts `k` to be `n - 1`. Finally, it prints the calculated sum for each test case.

