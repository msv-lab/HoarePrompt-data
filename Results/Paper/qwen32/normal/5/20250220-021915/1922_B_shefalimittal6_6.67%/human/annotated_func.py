#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        num_of_lens = {}
        
        nums = list(map(int, input().split()))
        
        for x in nums:
            num_of_lens[x] = num_of_lens.get(x, 0) + 1
        
        res = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += math.comb(cnt, 3)
            if cnt >= 2:
                total_sum = sum(i for i in num_of_lens.values() if i != cnt)
                res += math.comb(cnt, 2) * total_sum
        
        print(res)
        
    #State: The output state after the loop executes all the iterations is the cumulative sum of `math.comb(cnt, 3)` for each `cnt >= 3` and `math.comb(cnt, 2) * total_sum` for each `cnt >= 2` where `total_sum` is the sum of all counts in `num_of_lens` except the current `cnt` for each test case. The variable `t` remains unchanged, and `n` and `nums` are reinitialized for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the number of ways to choose three integers from the list such that at least two of them are the same, considering all possible pairs and their combinations with other distinct integers.

