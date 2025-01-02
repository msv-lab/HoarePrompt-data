#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 2·10^5 and -10^9 ≤ k ≤ 0; a1, a2, ..., an are integers representing the ratings of the participants, where 1 ≤ ai ≤ 10^9.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, k = rints()
    a, ans, s = rints(), [], 0
    for i in range(1, n):
        if s - (n - i - len(ans) - 1) * a[i] * (i - len(ans)) < k:
            ans.append(i + 1)
            n -= 1
        else:
            s += a[i] * (i - len(ans))
        
    #State of the program after the  for loop has been executed: - `n` will be the initial `n` minus the number of times the condition `s - (n - i - len(ans) - 1) * a[i] * (i - len(ans)) < k` was true.
    #   - `s` will be the sum of all `a[i] * (i - len(ans))` for each `i` where the condition was false.
    #   - `ans` will be a list of integers `i + 1` for each `i` where the condition was true.
    #   - `a` remains unchanged.
    #   - `k` remains unchanged.
    #
    #Output State:
    print('\n'.join(map(str, ans)))
#Overall this is what the function does:The function reads two integers `n` and `k`, and a list of `n` integers `a` from the standard input. It processes these inputs to generate a list `ans` of integers. For each index `i` from 1 to `n-1`, it checks if a certain condition involving `s`, `n`, `i`, `len(ans)`, and `a[i]` is less than `k`. If the condition is true, it appends `i + 1` to `ans` and decrements `n`. If the condition is false, it updates the sum `s`. After processing, it prints the elements of `ans` on separate lines. The final state of the program is that `n` is reduced by the number of times the condition was true, `s` is updated based on the condition being false, `ans` contains the indices where the condition was true, and `a` and `k` remain unchanged.

