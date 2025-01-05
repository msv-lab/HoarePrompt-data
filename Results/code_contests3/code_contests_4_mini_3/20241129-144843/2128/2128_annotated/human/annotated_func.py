#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 1000) representing the number of test cases, for each test case n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5) representing the number of barrels and the number of pourings, and a is a list of n integers (0 ≤ a_i ≤ 10^{9}) representing the initial amounts of water in each barrel, with the total sum of n over test cases not exceeding 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `ans` is equal to the maximum value in `arr` plus the sum of the first `min(k, n - 1)` elements of `arr`, `t` is the number of test cases, `n` is an integer representing the size of the array for each test case, `k` is an integer that determines how many elements to sum from the sorted array, and `arr` is a list of integers sorted in descending order for each test case.
#Overall this is what the function does:The function accepts multiple test cases where each test case consists of an integer `n` (the number of barrels) and `k` (the number of pourings), followed by a list of integers representing the initial amounts of water in each barrel. It calculates the maximum possible amount of water after performing up to `k` pourings, which is the sum of the largest amount in the list and the sum of the next `min(k, n - 1)` largest amounts. The function prints the result for each test case.

