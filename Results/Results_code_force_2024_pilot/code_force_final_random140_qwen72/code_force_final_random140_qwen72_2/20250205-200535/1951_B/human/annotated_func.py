#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two lines: the first line contains two integers n and k where 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n, representing the number of cows and the index of your cow, respectively. The second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, representing the Cowdeforces ratings of the cows, and all a_i's are distinct. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers from the input, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]` before encountering an element greater than `a[k - 1]`, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in `a` that are less than or equal to `a[k - 1]` before encountering an element greater than `a[k - 1]` and wins is greater than or equal to `k`)
    #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers from the input, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]` before encountering an element greater than `a[k - 1]`, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists. If `wins` is greater than or equal to `k`, the current value of `wins` remains unchanged.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers from the input, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]` before encountering an element greater than `a[k - 1]`, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists, `wins_with_swap` is the number of elements in `a` from `wins_with_swap` to `k - 1` that are less than or equal to `a[k - 1]` plus `wins + 1`.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)) (where wins is the number of elements in a that are less than or equal to a[k - 1] before encountering an element greater than a[k - 1], and wins_with_swap is the number of elements in a from wins_with_swap to k - 1 that are less than or equal to a[k - 1] plus wins + 1)
#Overall this is what the function does:The function processes multiple test cases, each involving a list of distinct Cowdeforces ratings for a group of cows. For each test case, it calculates and prints the maximum number of cows whose ratings are less than or equal to the rating of a specified cow (at index `k-1`), considering both the original list and a hypothetical scenario where the specified cow's rating is swapped with the next higher rating in the list. The function does not return any values; it only prints the results for each test case.

