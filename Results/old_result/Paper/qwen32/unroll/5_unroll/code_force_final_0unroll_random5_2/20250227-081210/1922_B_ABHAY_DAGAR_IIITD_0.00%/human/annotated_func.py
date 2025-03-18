#State of the program right berfore the function call: test_cases is a list of test cases where each test case is a list containing an integer n (1 ≤ n ≤ 3 · 10^5) followed by a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: results is a list containing the computed results for each test case.
    for result in results:
        print(result)
        
    #State: results is a list containing the computed results for each test case, and each result has been printed to the console.
#Overall this is what the function does:The function `func_1` processes a series of test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates a result based on the frequency of each integer in the list and prints this result. The function does not return any value directly but outputs the result for each test case to the console.

