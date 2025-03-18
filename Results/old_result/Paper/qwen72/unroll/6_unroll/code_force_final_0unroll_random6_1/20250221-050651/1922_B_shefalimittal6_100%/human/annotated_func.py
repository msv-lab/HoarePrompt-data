#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` representing the exponents of the stick lengths (2^{a_i}), and an integer `n` representing the number of sticks, where 1 \le n \le 3 \cdot 10^5 and 0 \le a_i \le n. The function should also handle multiple test cases, where the number of test cases `t` is an integer such that 1 \le t \le 10^4. The sum of `n` over all test cases does not exceed 3 \cdot 10^5.
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
        
    #State: `idx` is equal to the total number of elements in `data`, `t` is equal to `int(data[0])`, `results` is a list of strings where each string represents the number of ways to choose 2 or 3 sticks of the same length for each test case.
    print('\n'.join(results))
    #This is printed: - Since the exact values of the `results` list are not provided, we can only describe the structure of the output.
    #   - Each element of the `results` list will be printed on a new line.
    #
    #Output:
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and prints the number of ways to choose 2 or 3 sticks of the same length for each test case. Each test case consists of a list of integers representing the exponents of stick lengths (2^{a_i}), and the function outputs the results for each test case on a new line. The function does not return any value.

