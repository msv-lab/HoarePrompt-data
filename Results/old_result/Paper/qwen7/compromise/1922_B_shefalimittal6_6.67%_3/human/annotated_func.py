#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all 1 ≤ i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, `num_of_lens` is a dictionary containing the frequency of each unique value in all `nums` lists processed during the loop. The variable `res` is the cumulative result of adding `math.comb(cnt, 3)` for every `cnt` (frequency) that is 3 or more, and `math.comb(cnt, 2) * total_sum` for every `cnt` (frequency) that is 2 or more, where `total_sum` is the sum of all frequencies in `num_of_lens.values()` except for the current `cnt`. The variable `t` is set to 0 or negative, `n` retains its last input value, and `nums` is an empty list. The loop processes all values in `num_of_lens.values()` according to their conditions across all iterations.
    #
    #In simpler terms, `res` will be the sum of all combinations calculated based on the frequencies of numbers in all `nums` lists processed, specifically:
    #- For every frequency of 3 or more, add the combination of choosing 3 out of that frequency.
    #- For every frequency of 2 or more, add twice the product of the combination of choosing 2 out of that frequency and the sum of all other frequencies.
    #
    #All other variables (`t`, `n`, `nums`) remain unchanged and retain their final values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of the list), and a list `nums` of `n` non-negative integers. For each test case, it calculates and sums specific combinations based on the frequency of each unique number in `nums`. Specifically, it adds the combination of choosing 3 out of the frequency for each number that appears 3 or more times, and twice the product of the combination of choosing 2 out of the frequency and the sum of all other frequencies for each number that appears 2 or more times. The function outputs the cumulative result for each test case.

