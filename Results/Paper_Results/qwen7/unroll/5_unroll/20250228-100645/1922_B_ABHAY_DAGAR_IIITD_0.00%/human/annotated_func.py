#State of the program right berfore the function call: test_cases is a list of tuples. Each tuple contains two elements: an integer n (1 ≤ n ≤ 3 ⋅ 10^5) representing the number of sticks, and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents used to determine the lengths of the sticks as 2^{a_i}. The sum of all n values across all tuples does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `test_cases` is a list of tuples, each containing an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`, and `results` is a list of integers where each integer represents the calculated result based on the operations performed inside the loop for each corresponding test case.
    for result in results:
        print(result)
        
    #State: The output state will be a series of printed lines, each containing an integer from the `results` list, corresponding to the calculated result for each test case.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains an integer `n` and a list of `n` integers representing exponents used to determine stick lengths. For each test case, it calculates the number of unique triplets and pairs of sticks that can be formed, and sums these values. The function then returns a list of integers, where each integer corresponds to the calculated result for each test case.

