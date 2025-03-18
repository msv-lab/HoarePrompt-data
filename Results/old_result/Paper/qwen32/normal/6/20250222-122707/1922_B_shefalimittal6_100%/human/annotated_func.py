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
        
    #State: `t` is 0, `n` is the integer value at `data[idx]`, `a_1, a_2, ..., a_n`, `input`, `data` remain as given, `idx` is `idx + (total number of elements processed in all iterations)`, `cnt` is the sum of all elements in `v` for the last iteration, `ans` is the accumulated sum of combinations based on the conditions in the loop body for the last iteration, `results` now includes `str(ans)` for each of the `t` iterations.
    print('\n'.join(results))
    #This is printed: (an empty string)
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a_1, a_2, ..., a_n`. It calculates a value based on the frequency of each integer in the list and the combinations of these frequencies. The function outputs a single integer for each test case, representing the calculated value.

