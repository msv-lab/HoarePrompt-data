#State of the program right berfore the function call: test_cases is a list of test cases, where each test case is a list containing two elements: the first element is an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and the second element is a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents of the lengths of the sticks. The length of test_cases is an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `results` is a list containing the results of each test case, where each result is the number of ways to choose three sticks such that the product of their lengths is a perfect square. The lengths of the sticks are determined by 2 raised to the power of the exponents given in each test case. The length of `results` is equal to the number of test cases, and each element in `results` corresponds to the respective test case in `test_cases`.
    for result in results:
        print(result)
        
    #State: The `results` list remains unchanged, and each element in `results` is printed to the console in sequence.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a list containing an integer `n` and a list of `n` integers representing the exponents of the lengths of sticks. It processes each test case to calculate the number of ways to choose three sticks such that the product of their lengths is a perfect square. The lengths of the sticks are determined by 2 raised to the power of the exponents given in each test case. After processing all test cases, it prints each result to the console in sequence. The function does not return any value; instead, it modifies the state by printing the results.

