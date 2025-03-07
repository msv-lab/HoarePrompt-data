#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all 1 ≤ i ≤ n. The sum of all n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `results` is a list containing the string representations of `ans` for each iteration of the loop, `i` is `n`, `n` is `idx - 1`, `cnt` is the sum of all elements in `v`, and `ans` is the accumulated result from the loop's operations on `v` for all iterations.
    #
    #In simpler terms, after all iterations of the loop have finished, `results` will contain a list of strings where each string represents the value of `ans` calculated for each of the `t` iterations. The variable `n` will be equal to the last index processed (`idx - 1`), `cnt` will be the total count of all occurrences across all lists `v` for each iteration, and `ans` will hold the final accumulated result from performing the specified calculations over all iterations.
    print('\n'.join(results))
    #This is printed: the string representations of `ans` for each iteration, separated by newlines
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer \( t \) (number of test cases), a positive integer \( n \) (size of the list), and a list of non-negative integers \( a \) (of size \( n \)). For each test case, it calculates a specific value based on the frequency of elements in the list \( a \) and stores the result as a string in a list. Finally, it prints the results for all test cases, each result separated by a newline.

