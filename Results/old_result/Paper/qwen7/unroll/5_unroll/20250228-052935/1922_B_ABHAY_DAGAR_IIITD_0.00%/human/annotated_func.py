#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains two elements: an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `test_cases` is a list of tuples, each containing an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`, and `results` is a list of integers where each integer represents the calculated value of `res` for each test case after executing the loop.
    for result in results:
        print(result)
        
    #State: results is a list of integers where each integer represents the printed value of each result in the original results list.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of an integer `n` and a list of `n` integers representing exponents. For each test case, it calculates the number of ways to choose three or more identical exponents and pairs of identical exponents, then sums these values. The function returns a list of results, where each result corresponds to the calculated value for each test case.

