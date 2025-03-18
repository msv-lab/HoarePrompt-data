#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n; a is a list of n integers such that 1 ≤ a_i ≤ 10^9 and all a_i's are distinct.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: `wins` is between 0 and n (inclusive), depending on how many elements in list `a` are less than or equal to `a[k-1]`. `t`, `n`, `k`, and `a` remain unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in list `a` that are less than or equal to `a[k-1]`)
        return
        #The program does not return any value since there is no return statement in the provided code snippet.
    #State: `wins` is between 0 and n (inclusive), depending on how many elements in list `a` are less than or equal to `a[k-1]`. `t`, `n`, `k`, and `a` remain unchanged. Wins is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `wins` is between 0 and `k-1`, `win_with_swap` is between `wins + 1` and `k - 1`, `t`, `n`, `k`, and `a` remain unchanged.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: win_with_swap - wins
#Overall this is what the function does:The function processes a list of integers `a` and two integers `n` and `k`. It counts how many elements in `a` are less than or equal to the element at index `k-1`. If the count is greater than or equal to `k`, it prints `wins - 1`. Otherwise, it calculates a potential new count (`win_with_swap`) after swapping one element and prints the maximum of the original count or the new count minus the original count. The function does not return any value.

