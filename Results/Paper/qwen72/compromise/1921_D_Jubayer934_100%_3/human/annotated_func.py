#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `_` is a placeholder variable, `n` is a positive integer such that 1 ≤ n ≤ 100, `m` is a positive integer such that 1 ≤ m ≤ 100, `ans` is a list containing the absolute differences between each element of `a` and the corresponding element of `b` up to the index `i` where the loop breaks or completes. If `temp` is a non-negative integer such that 0 ≤ temp < n, `ans` contains the absolute differences from index `temp` to `n-1`, and `i` is `n-1`. If `temp` is -1, `ans` contains the absolute differences from index 0 to `n-1`, and `i` is `n-1`. The loop has completed all `t` test cases, and the sum of `ans` for each test case has been printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two lists of integers `a_i` and `b_i` with lengths `n` and `m` respectively. For each test case, it calculates the sum of the minimum absolute differences between elements of `a_i` and `b_i` by comparing each element of `a_i` with the corresponding element of `b_i` and the element at the mirrored position from the end of `b_i`. The function prints the sum of these minimum absolute differences for each test case. After processing all `t` test cases, the function concludes.

