#State of the program right berfore the function call: test_cases is a list of test cases, where each test case is a tuple containing two elements: the first element is an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and the second element is a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents of the lengths of the sticks. The length of the list test_cases is an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `test_cases` is a list of test cases with all test cases processed, `results` is a list containing the final value of `res` for each test case after all iterations, `num_list` is a list of integers provided by the input for the last test case, `num_of_lens` is a dictionary with all key-value pairs from the last `num_list`, `total_count` is the sum of all values in `num_of_lens` for the last test case, `x` is the last integer in the last `num_list`, `n` is the input integer for the last test case, and `res` is the final computed value for the last test case.
    for result in results:
        print(result)
        
    #State: `test_cases` is a list of test cases with all test cases processed, `results` is a list containing the final value of `res` for each test case after all iterations, `num_list` is a list of integers provided by the input for the last test case, `num_of_lens` is a dictionary with all key-value pairs from the last `num_list`, `total_count` is the sum of all values in `num_of_lens` for the last test case, `x` is the last integer in the last `num_list`, `n` is the input integer for the last test case, and `res` is the final computed value for the last test case.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing an integer `n` and a list of `n` integers representing the exponents of the lengths of sticks. It processes each test case to compute the number of ways to choose three sticks that can form a non-degenerate triangle, and stores these results in a list. After processing all test cases, it prints each result in the list. The function does not return any value; instead, it modifies the state by printing the results to the console. After the function concludes, `test_cases` remains unchanged, and the results of the computations are printed to the console.

