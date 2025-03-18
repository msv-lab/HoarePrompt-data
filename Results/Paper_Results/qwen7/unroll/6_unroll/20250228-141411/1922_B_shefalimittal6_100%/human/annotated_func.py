#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: idx is 2 + 2*t, t is t, n is an integer from data[0], a is a list of non-negative integers such that 0 ≤ a_i ≤ n, data is a list of strings obtained from splitting the input, results is a list of strings where each string is the result of the calculation for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: each string in the `results` list, each on a new line
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( t \) (number of test cases), a positive integer \( n \) (size of the list), and a list \( a \) of non-negative integers. For each test case, it calculates a specific value based on the frequency of elements in list \( a \) and stores the result. Finally, it prints these results, one per line.

