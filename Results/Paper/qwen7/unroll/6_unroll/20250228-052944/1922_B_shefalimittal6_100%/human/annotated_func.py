#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3⋅10^5, and the list a contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `idx` is 2 + 2*t, `t` is an integer such that 1 ≤ t ≤ 10^4, `results` is a list containing strings calculated from the loop executions.
    print('\n'.join(results))
    #This is printed: the contents of the `results` list, each item on a new line
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer t (number of cases), an integer n (size of the list), and a list a of n integers. It calculates a result based on the frequency of elements in the list a and appends the result to a list. Finally, it prints the results for all test cases, each on a new line.

