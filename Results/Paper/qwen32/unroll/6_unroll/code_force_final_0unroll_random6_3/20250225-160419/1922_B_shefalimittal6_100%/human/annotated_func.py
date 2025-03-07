#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        v = [0] * (n + 1)
        
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            v[x] += 1
        
        cnt = 0
        
        ans = 0
        
        for i in range(n + 1):
            if v[i] >= 2:
                ans += cnt * v[i] * (v[i] - 1) // 2
            if v[i] >= 3:
                ans += v[i] * (v[i] - 1) * (v[i] - 2) // 6
            cnt += v[i]
        
        results.append(str(ans))
        
    #State: - After all iterations, the `results` list will contain the results for each of the `t` test cases.
    #   - The `idx` variable will have been incremented by `2 + n` for each test case, where `n` is the number of integers in that test case.
    #   - The `t`, `data`, and other variables not modified by the loop will remain unchanged.
    #
    #Given the above explanation, the output state can be described as follows:
    #
    #Output State:
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the results for each of the t test cases)
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers. It calculates a specific value based on the frequency of each integer in the list and returns this value for each test case. The results for all test cases are printed, each on a new line.

