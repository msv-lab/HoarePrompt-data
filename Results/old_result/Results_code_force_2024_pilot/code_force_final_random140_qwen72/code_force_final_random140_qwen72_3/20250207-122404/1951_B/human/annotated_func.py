#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and k, where 2 ≤ n ≤ 10^5 and 1 ≤ k ≤ n, representing the number of cows and the index of your cow, respectively. The second line of each test case contains n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9, representing the Cowdeforces ratings of the cows. All a_i's are distinct. The sum of n over all test cases does not exceed 10^5.
def func_1():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers read from input, `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before encountering an element greater than `a[k-1]`, `i` is the index of the first element in `a` that is greater than `a[k-1]` or `n` if no such element exists.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in `a` that are less than or equal to `a[k-1]` before encountering an element greater than `a[k-1]`)
    #State: *`t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers read from input, `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before encountering an element greater than `a[k-1]`, and `i` is the index of the first element in `a` that is greater than `a[k-1]` or `n` if no such element exists. If `wins` is greater than or equal to `k`, the condition holds true.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 2 ≤ n ≤ 10^5, `k` is an integer where 1 ≤ k ≤ n, `a` is a list of integers read from input, `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before encountering an element greater than `a[k-1]`, `i` is the index of the first element in `a` that is greater than `a[k-1]` or `n` if no such element exists, `wins_with_swap` is the number of elements in `a` that are less than or equal to `a[k-1]` starting from `wins_with_swap` until the first element greater than `a[k-1]` is encountered or the end of the list is reached.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)) (where `wins` is the number of elements in `a` that are less than or equal to `a[k-1]` before encountering an element greater than `a[k-1]`, and `wins_with_swap` is the number of elements in `a` that are less than or equal to `a[k-1]` starting from `wins_with_swap` until the first element greater than `a[k-1]` is encountered or the end of the list is reached)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of cows `n`, the index of your cow `k`, and a list of Cowdeforces ratings `a`. For each test case, it calculates the number of cows whose ratings are less than or equal to your cow's rating (`a[k-1]`) before encountering a cow with a higher rating. If this count is greater than or equal to `k`, it prints the count minus one. Otherwise, it calculates the maximum possible number of cows that can be ahead of your cow after a potential swap, and prints this value. The function reads input from the standard input and prints the results to the standard output.

