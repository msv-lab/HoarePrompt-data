#State of the program right berfore the function call: The function should take three parameters: t (an integer representing the number of test cases, where 1 ≤ t ≤ 10^4), a list of tuples where each tuple contains two integers n and k (representing the number of cows and your cow's index, respectively, with 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n), and a list of lists where each sublist contains n integers a_1, a_2, ..., a_n (representing the Cowdeforces ratings of the cows, with 1 ≤ a_i ≤ 10^9 and all a_i's being pairwise different). The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: The value of `wins` will be the number of elements in the list `a` that are less than or equal to `a[k-1]` up to the point where an element greater than `a[k-1]` is encountered, or `n` if no such element is found. The values of `t`, `n`, `k`, and `a` remain unchanged.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in the list `a` that are less than or equal to `a[k-1]` up to the point where an element greater than `a[k-1]` is encountered, or `n` if no such element is found, and wins is greater than or equal to `k`)
        return
        #The program returns the current value of `wins`, which is greater than or equal to `k`.
    #State: The value of `wins` will be the number of elements in the list `a` that are less than or equal to `a[k-1]` up to the point where an element greater than `a[k-1]` is encountered, or `n` if no such element is found. The values of `t`, `n`, `k`, and `a` remain unchanged. Additionally, `wins` is less than `k`.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `win_with_swap` will be the number of elements in the list `a` that are less than or equal to `a[k-1]` from the initial `win_with_swap` position up to the point where an element greater than `a[k-1]` is encountered, or `k-1` if no such element is found. The values of `t`, `n`, `k`, and `a` remain unchanged.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: - The `max` function will return the larger of the two values:
    #     - `wins - 1`
    #     - `win_with_swap - wins` (if `wins` is not 0)
    #     - `win_with_swap - 1` (if `wins` is 0)
    #
    #### Final Output:
    #- If `wins` is not 0, the output will be the maximum of `wins - 1` and `win_with_swap - wins`.
    #- If `wins` is 0, the output will be the maximum of `wins - 1` (which is -1) and `win_with_swap - 1`.
    #
    #Since `wins - 1` is -1 when `wins` is 0, the `max` function will always return `win_with_swap - 1` in this case.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads input values for `n` and `k` (the number of cows and the index of your cow, respectively), and a list `a` of Cowdeforces ratings. It calculates the number of cows with ratings less than or equal to your cow's rating (`a[k-1]`) up to the point where a cow with a higher rating is encountered. If this number (`wins`) is greater than or equal to `k`, it prints `wins - 1`. Otherwise, it calculates the maximum number of cows that can be swapped to increase your cow's position and prints this value. The function does not return any value. The input parameters `t`, `cows_info`, and `ratings` are not directly used within the function, and the values of `n`, `k`, and `a` remain unchanged after the function call.

