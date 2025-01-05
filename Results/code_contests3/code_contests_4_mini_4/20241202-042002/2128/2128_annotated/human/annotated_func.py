#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 1000) representing the number of test cases; for each test case, n is an integer (1 ≤ k < n ≤ 2 ⋅ 10^5) representing the number of barrels, k is an integer representing the number of pourings, and a is a list of n integers (0 ≤ a[i] ≤ 10^9) representing the initial amounts of water in each barrel. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `i` is equal to `t`, `n` is the number of elements from the last test case, `k` is updated accordingly, `arr` is a list of integers (the last input list sorted in descending order), `ans` is the sum for the last test case and has been printed.
#Overall this is what the function does:The function accepts multiple test cases where each test case consists of an integer `n` (number of barrels), an integer `k` (maximum number of pourings), and a list `a` of integers representing the initial amounts of water in each barrel. It calculates the maximum amount of water that can be obtained by pouring from the `k` fullest barrels into the first barrel, and prints the total amount of water in the first barrel after the pourings for each test case. If `k` is greater than or equal to `n`, it adjusts `k` to `n - 1` to avoid exceeding the number of barrels. The function does not handle cases where `n` or `k` are outside the specified bounds, and assumes valid input as per the constraints.

