#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. test_cases is a list of t elements, where each element is a tuple (n, a) with n being an integer such that 1 <= n <= 3 * 10^5, and a being a list of n integers where each integer a_i satisfies 0 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: Output State: `data` remains a list of strings obtained by splitting the input read from the standard input stream, `idx` is the index after the last element processed in `data`, `t` is the integer value of `data[0]`, `results` is a list of strings where each string represents the number of ways to choose 2 or 3 identical elements from the sublists of integers derived from `data`.
    print('\n'.join(results))
    #This is printed: - The output will be a series of strings, each on a new line, representing the number of ways to choose 2 or 3 identical elements from the sublists of integers derived from `data`.
    #
    #Since the exact content of `data` and the sublists of integers are not provided, we can't determine the exact numerical values in `results`. However, we can describe the output based on the given information.
    #
    #Output:
#Overall this is what the function does:The function reads input from the standard input stream, processes a series of test cases, and prints the results. Each test case consists of an integer `n` and a list of `n` integers. The function calculates the number of ways to choose 2 or 3 identical elements from the list of integers for each test case and prints these counts, one per line. The function does not return any value; it only prints the results to the standard output. After the function concludes, `data` remains a list of strings obtained from the input, `idx` is the index after the last processed element in `data`, and `t` is the integer value of the first element in `data`.

