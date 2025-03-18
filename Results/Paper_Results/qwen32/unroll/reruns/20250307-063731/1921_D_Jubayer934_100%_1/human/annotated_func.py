#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 \cdot 10^5. a_i is a list of n integers where each integer satisfies 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where each integer satisfies 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: A series of sums, one for each test case, representing the sum of the absolute differences calculated as described.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives two lists of integers, `a` and `b`, and calculates the sum of absolute differences between corresponding elements of the sorted `a` and a specially ordered `b`. The ordering of `b` involves comparing elements from the start and end to determine the optimal pairing with `a`. The result for each test case is printed as the sum of these absolute differences.

