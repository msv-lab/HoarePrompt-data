#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n (1 ≤ n ≤ 3 · 10^5) integers a_1, a_2, ..., a_n (0 ≤ a_i ≤ n) representing the exponents of the lengths of the sticks. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: `t` is 0, `idx` is `len(data)`, `results` is a list containing `t` (initial `t`) string representations of `ans`, `n` is the integer value of `data[len(data) - 1 - n]` and must be greater than 0, `v` is a list of zeros with length `n + 1` where each `v[x]` (for each `x` read from `data` starting from the appropriate index to the end of `data`) is incremented by 1, `cnt` is the sum of all values in `v`, `x` is the integer value of the last element in `data`, `_` is `n - 1`, and `ans` is the sum of all combinations of 2 and 3 from the values in `v` that are greater than or equal to 2 and 3, respectively.
    print('\n'.join(results))
    #This is printed: 0
#Overall this is what the function does:The function reads input from `sys.stdin`, processes multiple test cases, and calculates the number of ways to pick 2 or 3 sticks with the same exponent of length. It then prints the results for each test case, one per line. The function does not return any value. After the function concludes, `t` is 0, `idx` is equal to the length of the input data, `results` contains the string representations of the calculated answers for each test case, and the variables `n`, `v`, `cnt`, `x`, and `ans` are in their final states as described in the annotated code.

