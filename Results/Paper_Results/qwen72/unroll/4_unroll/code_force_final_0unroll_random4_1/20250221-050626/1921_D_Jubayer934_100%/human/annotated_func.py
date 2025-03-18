#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5. a_i is a list of n integers where 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop reads `t` test cases, and for each test case, it reads `n` and `m`, two lists `a` and `b` of integers, and prints the sum of the minimum absolute differences between elements of `a` and `b`. The variables `t`, `n`, `m`, `a`, and `b` are reset for each test case, and the loop continues until all `t` test cases have been processed. The final state of these variables is undefined as they are re-initialized for each test case. The variable `ans` contains the list of absolute differences for the last test case, and `temp` is an integer that indicates the index where the algorithm decided to switch the pairing strategy, or -1 if no switch was needed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `m`, and two lists of integers `a` and `b`. For each test case, it calculates the sum of the minimum absolute differences between elements of `a` and `b` using a specific pairing strategy. The function reads the number of test cases `t` and processes each one, printing the sum of the minimum absolute differences for each test case. After processing all test cases, the function does not return any value, and the final state of the variables `t`, `n`, `m`, `a`, and `b` is undefined as they are re-initialized for each test case. The variable `ans` contains the list of absolute differences for the last test case, and `temp` is an integer that indicates the index where the algorithm decided to switch the pairing strategy, or -1 if no switch was needed.

