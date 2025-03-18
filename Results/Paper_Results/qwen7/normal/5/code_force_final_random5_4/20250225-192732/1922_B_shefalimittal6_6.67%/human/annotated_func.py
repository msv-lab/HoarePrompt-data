#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n non-negative integers such that 0 ≤ a_i ≤ n. Additionally, the sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: The final value of `res` will be the sum of all `math.comb(cnt, 3)` for each `cnt` in `num_of_lens.values()` that is greater than or equal to 3, plus the sum of all `math.comb(cnt, 2) * total_sum` for each `cnt` in `num_of_lens.values()` that is greater than or equal to 2 but less than 3, where `total_sum` is the sum of all values in `num_of_lens.values()` except the current `cnt`.
    #
    #In simpler terms, after the loop executes all its iterations, `res` will accumulate the combinatorial sums based on the counts of integers in `nums`, considering all possible combinations of 3 elements and pairs, as long as their counts meet the specified conditions. The `num_of_lens` dictionary will reflect the final count of each unique integer from the `nums` list after all iterations of the loop. The final value of `res` will be the sum of all these combinatorial calculations across all iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer t indicating the number of subsequent test cases, a positive integer n indicating the size of a list, and a list a of n non-negative integers. For each test case, it calculates the sum of specific combinatorial values based on the frequency of each unique integer in the list a. Specifically, it adds the number of ways to choose 3 elements from the frequency of each integer if the frequency is 3 or more, and the product of the number of ways to choose 2 elements from the frequency of each integer and the sum of frequencies of other integers if the frequency is 2. The function outputs the accumulated sum for each test case.

