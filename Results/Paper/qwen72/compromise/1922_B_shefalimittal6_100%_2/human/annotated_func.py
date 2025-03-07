#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains an integer n (1 ≤ n ≤ 3 · 10^5) followed by n integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n), representing the exponents of the lengths of the sticks. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `idx` is `len(data)`, `data` is a list of strings, `results` is a list containing the string representation of `ans` for each iteration of the loop, `n` is the last value of `n` processed, `v` is a list of `n + 1` zeros with each element at index `x` incremented by the number of times `x` appears in the corresponding segment of `data`, `cnt` is the sum of all elements in `v`, `i` is `n`, `x` is the integer value of `data[idx - 1]`, and `ans` is the sum of all combinations of pairs and triplets of elements in `v` that are greater than or equal to 2 and 3, respectively.
    print('\n'.join(results))
    #This is printed: [ans1]
    #[ans2]
    #...
    #[ansN] (where each [ansX] is the string representation of the value of `ans` for each iteration of the loop)
#Overall this is what the function does:The function reads input from standard input, processes `t` test cases, where each test case contains an integer `n` followed by `n` integers representing the exponents of the lengths of sticks. For each test case, it calculates the number of ways to choose pairs and triplets of sticks with the same exponent. The function then prints the results for each test case, with each result being the string representation of the calculated number of combinations. After the function concludes, `t` is 0, `idx` is equal to the length of the input data, `data` is a list of strings, `results` is a list of strings containing the results for each test case, and the final state of the program is that the results have been printed to the standard output.

