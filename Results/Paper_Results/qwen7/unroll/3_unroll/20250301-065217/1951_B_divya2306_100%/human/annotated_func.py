#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is between 0 and n (inclusive), depending on how many elements in `a` are less than or equal to `a[k - 1]`. `t`, `n`, `k`, and `a` remain unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is a value greater than or equal to k)
        return
        #The program returns the current value of wins, which is greater than or equal to k
    #State: `wins` is between 0 and n (inclusive), depending on how many elements in `a` are less than or equal to `a[k - 1]`. `t`, `n`, `k`, and `a` remain unchanged. Wins is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `wins` is between 0 and `n` (inclusive) and is less than `k`; `win_with_swap` is the minimum value between `wins + 1` and the index of the first element in `a` from `win_with_swap` to `k-2` that is greater than `a[k-1]`. If no such element exists, `win_with_swap` equals `k - 1`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: 1
#Overall this is what the function does:The function processes predefined variables \( t \), \( n \), \( k \), and \( a \). It counts how many elements in the list \( a \) are less than or equal to the \( k \)-th smallest element in \( a \). Depending on the count, it either returns \( \text{wins} - 1 \) if \( \text{wins} \geq k \), or calculates and returns the maximum of \( \text{wins} - 1 \) and \( \text{win\_with\_swap} - \text{wins} - 1 + (\text{wins} \neq 0) \) if \( \text{wins} < k \).

