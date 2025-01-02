#State of the program right berfore the function call: n, k, and d are integers such that 1 ≤ k ≤ n ≤ 5·10^5 and 0 ≤ d ≤ 10^9. a is a list of n integers where 1 ≤ ai ≤ 10^9.
def func():
    [n, k, d] = map(int, raw_input().strip().split())
    ais = list(map(int, raw_input().strip().split()))
    if (k == 1) :
        print('YES')
        exit()
    #State of the program after the if block has been executed: *`n`, `k`, and `d` are updated to the integer values provided by the user, 1 ≤ k ≤ n ≤ 5·10^5, 0 ≤ d ≤ 10^9, `a` is a list of n integers where 1 ≤ ai ≤ 10^9, `ais` is a list of `n` integers. If `k` is 1, the program has terminated.
    ais.sort()
    cando = [(False) for _ in range(n)]
    j = n - 1
    count = 0
    for i in reversed(range(n)):
        if i + k < n and cando[i + k]:
            count += 1
        
        if n - i < k:
            continue
        
        if ais[-1] - ais[i] <= d:
            cando[i] = True
            continue
        
        while ais[j - 1] > ais[i] + d:
            if cando[j]:
                count -= 1
            j -= 1
        
        cando[i] = count > 0
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is an integer such that 1 ≤ k ≤ n, `d` is an integer such that 0 ≤ d ≤ 10^9, `a` is a list of `n` integers where 1 ≤ ai ≤ 10^9, `ais` is a list of `n` integers sorted in ascending order, `cando` is a list of `n` values where `cando[i]` is `True` if there exists a valid subsequence of length `k` starting at `i` that satisfies the condition `ais[j] - ais[i] <= d` for all elements in the subsequence, and `False` otherwise, `j` is the largest index such that `ais[j - 1] <= ais[0] + d` or 0 if no such index exists, `count` is the final value of `count` based on the number of valid subsequences found during the loop execution.
    if cando[0] :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `k` is an integer such that 1 ≤ k ≤ n, `d` is an integer such that 0 ≤ d ≤ 10^9, `a` is a list of `n` integers where 1 ≤ ai ≤ 10^9, `ais` is a list of `n` integers sorted in ascending order, `cando` is a list of `n` values where `cando[i]` is `True` if there exists a valid subsequence of length `k` starting at `i` that satisfies the condition `ais[j] - ais[i] <= d` for all elements in the subsequence, and `False` otherwise, `j` is the largest index such that `ais[j - 1] <= ais[0] + d` or 0 if no such index exists, and `count` is the final value of `count` based on the number of valid subsequences found during the loop execution. If `cando[0]` is `True`, then `cando[0]` remains `True`. If `cando[0]` is `False`, then `cando[0]` remains `False`.
#Overall this is what the function does:The function `func()` reads two lines of input: the first line contains three integers `n`, `k`, and `d`, and the second line contains a list of `n` integers `a`. It then checks if there exists a subsequence of length `k` in the list `a` such that the difference between the maximum and minimum elements in the subsequence is less than or equal to `d`. If such a subsequence exists, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. The function handles the edge case where `k` is 1 by immediately printing 'YES' and exiting. The function also ensures that the input constraints are respected: `1 ≤ k ≤ n ≤ 5·10^5`, `0 ≤ d ≤ 10^9`, and `1 ≤ ai ≤ 10^9`. The function does not handle invalid input formats or out-of-bound values gracefully; it assumes that the input is always valid.

