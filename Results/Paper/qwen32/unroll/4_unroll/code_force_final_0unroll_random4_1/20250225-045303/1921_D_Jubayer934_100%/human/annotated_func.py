#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each test case consists of three lines: the first line contains two integers n and m such that 1 <= n <= m <= 2 * 10^5. The second line contains n integers a_i such that 1 <= a_i <= 10^9. The third line contains m integers b_i such that 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: A series of sums, each representing the total of the minimum absolute differences for each test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it calculates the total of the minimum absolute differences between elements of two lists, `a` and `b`, under specific pairing rules, and prints the result for each test case.

