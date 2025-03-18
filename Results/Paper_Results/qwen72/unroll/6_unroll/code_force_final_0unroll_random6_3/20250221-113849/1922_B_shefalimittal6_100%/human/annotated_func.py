#State of the program right berfore the function call: The function `func_1` is expected to take input parameters, but the provided function definition does not include any. The correct function definition should include parameters for the number of test cases `t` and for each test case, the number of sticks `n` and a list of integers `a` representing the exponents of the stick lengths. The inputs should satisfy the constraints: 1 ≤ t ≤ 10^4, 1 ≤ n ≤ 3 × 10^5, and 0 ≤ a_i ≤ n, with the additional constraint that the sum of n over all test cases does not exceed 3 × 10^5.
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
        
    #State: `idx` is 12, `t` is the integer value of `data[0]`, `results` is a list containing the string representations of the calculated values of `ans` for each test case.
    print('\n'.join(results))
    #This is printed: Each string in the `results` list, one per line (where `results` is a list containing the string representations of the calculated values of `ans` for each test case)
#Overall this is what the function does:The function `func_1` reads input from standard input, processes multiple test cases, and prints the results. Each test case involves a number of sticks `n` and a list of integers `a` representing the exponents of the stick lengths. The function calculates the number of ways to choose pairs and triplets of sticks with the same exponent and appends these counts to a list `results`. After processing all test cases, it prints the counts, one per line, as string values. The function does not return any value.

