#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. The sum of all n values across all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `results` is a list of integers where each integer represents the number of ways to choose three sticks with the same exponent such that their combined length is divisible by 3, plus the number of ways to choose two sticks with the same exponent and multiply it by the number of sticks already considered, for each test case.
    for result in results:
        print(result)
        
    #State: The output state is a list of integers where each integer is the value printed by `print(result)` for each corresponding `result` in the original `results` list.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains the number of sticks and their corresponding exponents. It calculates the number of ways to choose three sticks with the same exponent such that their combined length is divisible by 3, and the number of ways to choose two sticks with the same exponent and multiply it by the number of sticks already considered, for each test case. The function then prints these calculated values for each test case.

