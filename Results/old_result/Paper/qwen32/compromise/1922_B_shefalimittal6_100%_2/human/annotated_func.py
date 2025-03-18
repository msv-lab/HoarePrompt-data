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
        
    #State: `t` is the total number of test cases, `n` is the number of elements in the last test case, `a_1, a_2, ..., a_n` are the integers for the last test case, `input` is the original input string, `data` is the list of strings from the input, `idx` is the position after the last test case, and `results` is a list of strings representing `ans` for each test case.
    print('\n'.join(results))
    #This is printed: Each string in the `results` list, separated by newline characters (where each string in the `results` list represents the answer for a specific test case)
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates a value based on the frequency of integers in the list and outputs the result for each test case.

