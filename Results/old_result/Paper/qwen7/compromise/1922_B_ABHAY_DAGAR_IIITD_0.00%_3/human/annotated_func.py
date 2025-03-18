#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. Additionally, the sum of all n values across all tuples does not exceed 3 ⋅ 10^5.
def func_1(test_cases):
    results = []
    for _ in range(test_cases):
        n = int(input())
        
        num_list = list(map(int, input().split()))
        
        num_of_lens = {}
        
        for x in num_list:
            if x in num_of_lens:
                num_of_lens[x] += 1
            else:
                num_of_lens[x] = 1
        
        res = 0
        
        total_count = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += cnt * (cnt - 1) * (cnt - 2) // 6
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2 * total_count
            total_count += cnt
        
        results.append(res)
        
    #State: Output State: The `results` list will contain the sum of all `res` values calculated for each iteration of the loop. For each iteration, `res` is computed based on the counts of each exponent value in the `num_of_lens` dictionary. Specifically, for each count `cnt` in `num_of_lens`, if `cnt` is 3 or more, the contribution to `res` is `cnt * (cnt - 1) * (cnt - 2) // 6`. If `cnt` is 2 or more, the contribution is `cnt * (cnt - 1) // 2 * total_count`, where `total_count` is the sum of all counts in `num_of_lens`. After all iterations, `results` will contain one element for each test case, representing the total number of unique triplets of sticks that can be formed for each set of inputs provided.
    #
    #In numerical terms, `results` will be a list where each element corresponds to the sum of all valid combinations of stick lengths that meet the criteria specified in the loop for each test case.
    for result in results:
        print(result)
        
    #State: Output State: The `results` list will contain the sum of all `res` values calculated for each iteration of the loop, with each `res` value being computed based on the counts of each exponent value in the `num_of_lens` dictionary for each test case. After all iterations, `results` will be a list where each element represents the total number of unique triplets of sticks that can be formed for each set of inputs provided across all iterations.
    #
    #In simpler terms, the final output state will be a list where each element is the total count of unique triplets of sticks that can be formed from the given lengths for each test case, after processing all iterations of the loop.
#Overall this is what the function does:The function processes a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. For each tuple, it calculates the total number of unique triplets of sticks that can be formed based on the counts of each exponent value. The function returns a list of results, where each result corresponds to the total count of unique triplets for each set of inputs provided.

