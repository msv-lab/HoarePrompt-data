#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple represents a test case. Each tuple contains an integer n (1 ≤ n ≤ 3 · 10^5) and a list of integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `results` is a list containing the computed `res` for each test case in `test_cases`.
    for result in results:
        print(result)
        
    #State: `results` is a list containing the computed `res` for each test case in `test_cases` and all elements in `results` have been printed.
#Overall this is what the function does:The function `func_1` processes a series of test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a result based on the frequency of elements in the list and prints this result. Specifically, it computes the number of ways to choose 3 elements of the same value and adds it to the number of ways to choose 2 elements of the same value multiplied by the total count of elements processed so far. After processing all test cases, all results are printed.

