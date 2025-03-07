#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. The list a contains n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise distinct. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; The list `a` contains `n` integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise distinct; The sum of `n` over all test cases does not exceed 10^5; `wins` is the number of elements in `a` that are less than or equal to `a[k-1]`.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: k - 1
        return
        #The program returns nothing.
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; The list `a` contains `n` integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise distinct; The sum of `n` over all test cases does not exceed 10^5; `wins` is the number of elements in `a` that are less than or equal to `a[k-1]`; `wins` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `t` remains the same; `n` remains the same; `k` remains the same; `a` remains the same; `wins` remains the same; `win_with_swap` is the position just after the last element in `a` that is less than or equal to `a[k-1]` or `k - 1` if all elements from `win_with_swap` to `k-2` are less than or equal to `a[k-1]`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins - 1 + (wins != 0)) (where wins is the given number of wins and win_with_swap is the position just after the last element in a that is less than or equal to a[k-1] or k - 1 if all elements from win_with_swap to k-2 are less than or equal to a[k-1])
#Overall this is what the function does:The function `func_1` reads input for multiple test cases, where each test case consists of two integers `n` and `k`, and a list `a` of `n` distinct integers. For each test case, it calculates and prints the maximum number of positions that can be won by potentially swapping elements in the list `a` up to the `k`-th position, based on the values of the elements relative to `a[k-1]`. The function does not return any value.

