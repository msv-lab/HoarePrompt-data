#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a_1, a_2, ..., a_n are integers such that 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is an integer equal to `int(data[0])`; n is the last value of `n` read from the `data` list during the last iteration of the loop; a_1, a_2, ..., a_n are the last set of integers read from the `data` list during the last iteration of the loop; input is assigned the value of the input read from standard input; data is a list of strings, each representing one of the space-separated values from the input; idx is the index after the last integer read during the last iteration of the loop; results is a list containing the results for each of the t test cases.
    print('\n'.join(results))
    #This is printed: Each result from the test cases, separated by newlines (where each result is an element in the `results` list)
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input. Each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a result based on the frequency of each integer in the list and outputs the results for all test cases, each on a new line.

