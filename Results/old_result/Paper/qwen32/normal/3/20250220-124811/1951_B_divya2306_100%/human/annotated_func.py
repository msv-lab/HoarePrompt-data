#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise different. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise different; wins is the number of elements in a that are not greater than a[k-1]; i is n-1 if the loop completes all iterations without breaking, otherwise the index where a[i] > a[k-1].
    if (wins >= k) :
        print(wins - 1)
        #This is printed: the number of elements in the list `a` that are strictly less than `a[k-1]`
        return
        #The program returns nothing (None)
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise different; wins is the number of elements in a that are not greater than a[k-1]; i is n-1 if the loop completes all iterations without breaking, otherwise the index where a[i] > a[k-1]; wins is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` and `k` are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; `a` is a list of `n` integers such that 1 ≤ a_i ≤ 10^9 and all a_i are pairwise different; `wins` is the number of elements in `a` that are not greater than `a[k-1]` and `wins` is less than k; `i` is the index where `a[i] > a[k-1]` if such an index exists, otherwise `k - 1`; `win_with_swap` is the number of elements from index `win_with_swap` to `k - 2` that are not greater than `a[k-1]`, plus the initial `win_with_swap`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: wins - 1 (where wins is the number of elements in `a` that are not greater than `a[k-1]` and is less than `k`)
#Overall this is what the function does:The function reads integers `n` and `k`, and a list `a` of `n` integers. It calculates and prints the number of elements in `a` that are strictly less than `a[k-1]`, considering possible swaps to maximize this count without exceeding `k` elements. The function does not return any value.

