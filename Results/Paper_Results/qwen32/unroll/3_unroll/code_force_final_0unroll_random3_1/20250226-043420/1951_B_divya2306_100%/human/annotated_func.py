#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 2 <= n <= 10^5 and 1 <= k <= n. a is a list of n integers such that 1 <= a_i <= 10^9 and all a_i are pairwise different. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: t is unchanged; n is unchanged; k is unchanged; a is unchanged; wins is the count of elements in a from index 0 to k-2 that are less than or equal to a[k-1].
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the count of elements in the list `a` from index 0 to `k-2` that are less than or equal to `a[k-1]` and is greater than or equal to `k`)
        return
        #The program returns nothing (None)
    #State: t is unchanged; n is unchanged; k is unchanged; a is unchanged; wins is the count of elements in a from index 0 to k-2 that are less than or equal to a[k-1]; wins is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: - `t`, `n`, `k`, and `a` remain unchanged.
    #   - `wins` remains unchanged.
    #   - `win_with_swap` will be the count of elements in `a` from index `win_with_swap` to `k-2` that are less than or equal to `a[k-1]`, plus the initial `wins + 1`.
    #
    #Given this understanding, the output state can be described as:
    #
    #Output State:
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins - 1 + (wins != 0)) (where win_with_swap is the count of elements in `a` from index `win_with_swap` to `k-2` that are less than or equal to `a[k-1]`, plus the initial `wins + 1`)
#Overall this is what the function does:The function `func_1` processes a test case consisting of two integers `n` and `k`, and a list `a` of `n` integers. It calculates and prints the maximum number of elements in the list `a` from index `0` to `k-2` that are less than or equal to `a[k-1]`, considering possible swaps, without modifying the input values. The function does not return any value.

