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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, data is a list of strings representing the input values, idx is 1 + 2*t, results is a list of t strings representing the results of each test case.
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the strings in the results list)
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it calculates a result based on the frequency of integers in a given list and outputs the result for each test case. The output consists of `t` lines, where each line corresponds to the result of a test case.

