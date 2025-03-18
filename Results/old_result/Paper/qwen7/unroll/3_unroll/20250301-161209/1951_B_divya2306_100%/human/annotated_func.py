#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is between 0 and `k`, inclusive. `t` remains unchanged, and `k` remains unchanged. `a` remains unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: k - 1 (where k is the initial value of wins)
        return
        #The program returns None
    #State: `wins` is between 0 and `k`, inclusive, `t` remains unchanged, and `k` remains unchanged, `a` remains unchanged, and `wins` is less than `k`
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `wins` is now `wins` + 1, `t` remains unchanged, and `k` remains unchanged, `a` remains unchanged, `win_with_swap` is now the maximum of `win_with_swap` and `win_with_swap + 1` if the condition in the loop is never met, otherwise it is `win_with_swap + 1`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins, win_with_swap - (wins + 1) - 1 + (wins != 0)) (where `wins` is `wins + 1` and `win_with_swap` is updated based on the loop condition)
#Overall this is what the function does:The function processes a list of integers `a` of length `n` and finds the maximum number of elements in `a` that are greater than the `k-th` smallest element in `a`. If swapping the `k-th` smallest element with another element in the list increases the count of such elements, it considers this swap. The function then prints the maximum possible count of elements greater than the `k-th` smallest element, either before or after a potential swap, and returns `None`.

