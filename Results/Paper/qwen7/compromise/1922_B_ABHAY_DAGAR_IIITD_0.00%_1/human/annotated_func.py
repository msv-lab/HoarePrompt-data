#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: The `results` list will contain the sum of `res` values calculated for each test case. For each test case, `num_of_lens` will be a dictionary containing the frequency of each integer in the corresponding `num_list`. The `total_count` will be the sum of all values in `num_of_lens` for that test case. The `res` variable will hold the cumulative sum of contributions calculated according to the conditions given for each test case. `n` and `test_cases` will remain as they were initialized, and `num_list` will be an empty list for each test case.
    #
    #In simpler terms, after all iterations of the loop, the `results` list will contain one element for each test case, where each element represents the final value of `res` for that specific test case. The `num_of_lens` dictionary will store the frequency of numbers in the input lists for each test case, and `total_count` will be the sum of these frequencies. The `res` variable will accumulate the result based on the given conditions over all test cases.
    for result in results:
        print(result)
        
    #State: The `results` list will contain the final value of `res` for each test case after all iterations of the loop have finished.
#Overall this is what the function does:The function processes a list of tuples, where each tuple contains an integer \( n \) (representing the number of sticks) followed by \( n \) integers (exponents). For each tuple, it calculates a sum based on the frequency of each exponent and stores the result in a list. Finally, it prints each result from the list.

