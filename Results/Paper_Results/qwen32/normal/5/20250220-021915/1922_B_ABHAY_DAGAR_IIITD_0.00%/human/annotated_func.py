#State of the program right berfore the function call: test_cases is a list of test cases where each test case is a tuple (n, a) such that n is an integer (1 ≤ n ≤ 3 · 10^5) and a is a list of n integers (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `test_cases` is an empty list; `results` is a list containing the computed `res` values for each test case; `n`, `num_list`, `num_of_lens`, `res`, and `total_count` do not exist as they are local to each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `test_cases` is an empty list, `results` is a list containing all computed `res` values.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a result based on the number of ways to choose combinations of three or more identical integers and pairs of identical integers in relation to previously processed integers. The function prints the result for each test case.

