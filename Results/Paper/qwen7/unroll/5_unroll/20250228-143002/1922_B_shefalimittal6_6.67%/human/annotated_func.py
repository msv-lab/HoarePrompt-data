#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all i where 1 ≤ i ≤ n. The sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each value of t, there is a corresponding value of res calculated from the loop's operations. The variable res is the sum of combinations based on the frequency of numbers in the input lists. The other variables remain in their initial state.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `t` indicating the number of subsequent test cases, a positive integer `n`, and a list `a` of non-negative integers. For each test case, it calculates and sums up specific combinations based on the frequency of numbers in the list `a`. The final output is the cumulative sum of these combinations for all test cases.

