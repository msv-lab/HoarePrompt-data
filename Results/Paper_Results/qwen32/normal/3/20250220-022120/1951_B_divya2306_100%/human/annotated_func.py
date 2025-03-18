#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are distinct. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers read from the input such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; `a` is a list of `n` integers read from the input such that 1 ≤ a_i ≤ 10^9 and all a_i are distinct; `wins` is n.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is at least k)
        return
        #The program returns nothing (None) because the return statement is empty.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers read from the input such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; `a` is a list of `n` integers read from the input such that 1 ≤ a_i ≤ 10^9 and all a_i are distinct; `wins` is less than k.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 2 ≤ n ≤ 10^5, `k` is an integer such that 2 ≤ k ≤ n, `a` is a list of `n` integers read from the input such that 1 ≤ a_i ≤ 10^9 and all a_i are distinct, `wins` is less than k - 1, `win_with_swap` is k - 1.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: k - wins - 2 + (wins != 0)
#Overall this is what the function does:The function reads an integer `n`, another integer `k`, and a list of `n` distinct integers `a`. It calculates and prints the maximum number of participants that can be placed before the `k`-th participant in a sorted list without exceeding the `k`-th participant's value, considering a possible swap of the `k`-th participant with one of the participants that can be placed after it. The function does not return any value.

