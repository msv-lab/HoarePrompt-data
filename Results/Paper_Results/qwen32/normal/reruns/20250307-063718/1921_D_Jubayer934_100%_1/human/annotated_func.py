#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n <= m <= 2 * 10^5. a_i is a list of n integers where each a_i satisfies 1 <= a_i <= 10^9. b_i is a list of m integers where each b_i satisfies 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: t test cases have been processed, each with its own n and m values, a list of n integers, and a list of m integers. For each test case, the loop calculates the sum of the absolute differences between elements of two lists: `a` and `b`. The list `a` is sorted in ascending order, and `b` is sorted in descending order. The loop iterates through each element of `a` and compares the absolute difference between `a[i]` and `b[i]` with the absolute difference between `a[i]` and `b[-(n - i)]`. If the latter difference is larger, it switches to using `b[-(n - i)]` for the remaining elements of `a`. The final output for each test case is the sum of these absolute differences.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two lists of integers. For each test case, it calculates the sum of the absolute differences between elements of the two lists, with specific rules for selecting elements from the second list, and outputs this sum.

