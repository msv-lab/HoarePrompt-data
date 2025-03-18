#State of the program right berfore the function call: test_cases is a list of test cases, where each test case is a list containing two elements: the first element is an integer n (1 ≤ n ≤ 3 · 10^5) representing the number of sticks, and the second element is a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents of the lengths of the sticks. The length of the list test_cases is an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The `results` list will contain the number of ways to form triangles for each test case, and the `test_cases` list will remain unchanged.
    for result in results:
        print(result)
        
    #State: Output State: The `results` list remains unchanged, and the `test_cases` list remains unchanged. The loop has printed each element in the `results` list to the console, but the variables themselves are not modified by the loop.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a list containing an integer `n` and a list of `n` integers representing the exponents of the lengths of sticks. It processes each test case to calculate the number of ways to form triangles using the sticks and appends these counts to a list `results`. After processing all test cases, it prints each result to the console. The function does not return any value, but the `results` list contains the number of ways to form triangles for each test case, and the `test_cases` list remains unchanged.

