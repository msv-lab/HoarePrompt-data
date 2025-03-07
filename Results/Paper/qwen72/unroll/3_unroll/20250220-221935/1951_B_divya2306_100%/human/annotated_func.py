#State of the program right berfore the function call: The function should take two parameters: `n` and `k`, where `n` is the number of cows (2 ≤ n ≤ 10^5) and `k` is the index of your cow (1 ≤ k ≤ n). Additionally, it should take a list `a` of `n` distinct integers (1 ≤ a_i ≤ 10^9) representing the Cowdeforces ratings of the cows. The function should be able to handle multiple test cases, with the number of test cases `t` (1 ≤ t ≤ 10^4) provided as input. The sum of `n` over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before the first element greater than `a[k-1]` is encountered, or `n` if no such element exists. `n`, `k`, `a`, and `t` remain unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in `a` that are less than or equal to `a[k-1]` before the first element greater than `a[k-1]` is encountered, or `n` if no such element exists, and wins is greater than or equal to `k`)
        return
        #The program returns `wins`, which is the number of elements in `a` that are less than or equal to `a[k-1]` before the first element greater than `a[k-1]` is encountered, or `n` if no such element exists, and `wins` is greater than or equal to `k`.
    #State: `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before the first element greater than `a[k-1]` is encountered, or `n` if no such element exists. `n`, `k`, `a`, and `t` remain unchanged. `wins` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `win_with_swap` is the number of elements in `a` that are less than or equal to `a[k-1]` from `wins` to `k-1`, or `k` if no such element exists. `wins` remains unchanged. `n`, `k`, `a`, and `t` remain unchanged.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins if wins != 0 else win_with_swap - 1) (where `wins` is the value of `wins`, and `win_with_swap` is the number of elements in `a` that are less than or equal to `a[k-1]` from `wins` to `k-1`, or `k` if no such element exists)
#Overall this is what the function does:The function `func_1` takes no parameters and reads input from the standard input. It processes multiple test cases, each consisting of the number of cows `n`, the index of your cow `k`, and a list `a` of `n` distinct integers representing the Cowdeforces ratings of the cows. For each test case, it calculates and prints the maximum number of cows with ratings less than or equal to your cow's rating that can be placed before your cow, either without swapping or by swapping one cow. The function does not return any value. The state of `n`, `k`, `a`, and `t` remains unchanged after the function execution.

