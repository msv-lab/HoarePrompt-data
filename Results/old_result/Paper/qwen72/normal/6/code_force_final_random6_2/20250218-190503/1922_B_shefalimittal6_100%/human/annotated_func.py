#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) for a test case (1 ≤ n ≤ 3 · 10^5). The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has executed `t` times, `idx` is `1 + t * (n + 1)`, `results` is a list containing `t` strings, each string representing the calculated `ans` for each iteration, `n` is the last processed value of `n`, `v` is the last processed list of counts, `cnt` is the last processed sum of counts, and `ans` is the last processed answer.
    print('\n'.join(results))
    #This is printed: [ans_1]
    #[ans_2]
    #...
    #[ans_t] (where [ans_1], [ans_2], ..., [ans_t] are the string representations of the `ans` values calculated in each of the `t` iterations)
#Overall this is what the function does:The function reads input from standard input, processes `t` test cases, where each test case consists of an integer `n` followed by `n` integers. For each test case, it calculates the number of ways to choose pairs and triplets of the same integer from the list, and appends the result as a string to a list. Finally, it prints each result on a new line. The function does not return any value.

