#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `a_i` is -1, `i` is `n-1`, `m` is an input integer, `a` is a list of the first `n` integers from the sorted input, `b` is a list of the first `m` integers from the sorted input in descending order, `n` is an input integer, `ans` is a list containing the absolute differences between `a[i]` and `b[i]` for all `i` from 0 to `n-1`. If `temp` is not -1, then `temp` is an integer such that `temp < n`, and `ans` also contains the absolute differences between `a[i]` and `b[-(n - i)]` for all `i` from `temp` to `n-1`. Otherwise, `temp` remains -1.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads two integers `n` and `m`, and two lists of integers `a` and `b`. It calculates the sum of the absolute differences between elements of `a` and `b` in a specific order: initially, it pairs elements from the start of `a` with elements from the start of `b` in descending order. If at any point the absolute difference between the current element of `a` and the corresponding element from the end of `b` is greater than the difference with the current element of `b`, it switches to pairing elements from the start of `a` with elements from the end of `b` for the remaining elements. The function prints the sum of these absolute differences for each test case. After processing all test cases, `t` is 0, and the final state includes the processed lists `a` and `b` for each test case, and the list `ans` containing the absolute differences.

