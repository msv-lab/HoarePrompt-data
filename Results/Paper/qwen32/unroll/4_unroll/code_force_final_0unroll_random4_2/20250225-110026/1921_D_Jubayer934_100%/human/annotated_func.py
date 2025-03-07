#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5. a_i is a list of n integers where each a_i satisfies 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where each b_i satisfies 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The sum of the calculated differences for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers `a` and `b`. For each test case, it calculates the sum of the absolute differences between elements of `a` and `b` in a specific pairing strategy and outputs this sum.

