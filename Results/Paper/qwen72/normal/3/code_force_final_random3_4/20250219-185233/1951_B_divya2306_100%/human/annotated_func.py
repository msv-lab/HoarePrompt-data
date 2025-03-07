#State of the program right berfore the function call: The function should take two parameters: a list of integers `ratings` representing the Cowdeforces ratings of the cows, and an integer `k` representing the index of your cow. The length of `ratings` is `n` (2 ≤ n ≤ 10^5), and `1 ≤ k ≤ n`. Each rating in `ratings` is a distinct integer (1 ≤ a_i ≤ 10^9). The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^4). The sum of `n` over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `ratings` is a list of integers, `k` is an integer, `n` is the length of the `ratings` list, `t` is the number of test cases, `a` is a list of integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]` starting from the beginning of the list up to the first element that is greater than `a[k - 1]`, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in `a` that are less than or equal to `a[k - 1]` up to the first element that is greater than `a[k - 1]`)
        return
        #The program returns nothing.
    #State: `ratings` is a list of integers, `k` is an integer, `n` is the length of the `ratings` list, `t` is the number of test cases, `a` is a list of integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]` starting from the beginning of the list up to the first element that is greater than `a[k - 1]`, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists, and `wins` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `i` is the index of the first element in `a` that is greater than `a[k - 1]` starting from `win_with_swap`, or `k - 1` if no such element exists. `win_with_swap` is the number of elements in `a` that are less than or equal to `a[k - 1]` starting from `win_with_swap` up to `k - 1`. `k` remains unchanged.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: max(wins - 1, win_with_swap - wins) (if wins is not 0) or win_with_swap - 1 (if wins is 0)
#Overall this is what the function does:The function `func_1` accepts no parameters and reads input from the user. It processes a list of integers `ratings` and an integer `k` to determine the relative standing of the cow at index `k-1` based on the ratings. Specifically, it counts the number of cows with ratings less than or equal to the cow at index `k-1` from the beginning of the list up to the first cow with a higher rating. If this count is greater than or equal to `k`, it prints the count minus one. Otherwise, it calculates the maximum number of cows that can be swapped with the cow at index `k-1` to increase its standing and prints this value. The function does not return any value.

