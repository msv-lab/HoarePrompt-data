#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The output state consists of `t` lines, each representing the result `res` calculated for the corresponding input list in each iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates a value based on the combinations of numbers in the list and prints this value. Specifically, it counts the number of ways to choose 3 or more identical numbers and the number of ways to choose 2 identical numbers multiplied by the sum of counts of all different numbers, and sums these values to produce the result for each test case.

