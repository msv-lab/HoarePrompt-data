#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 3⋅10^5, and the list a contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `results` is a list containing the string representation of the final value of `ans` after all iterations of the loop have completed, `cnt` is the total count of non-zero elements in the list `v` summed across all iterations, `idx` is equal to `3 * t + 1`, and `ans` is the cumulative sum of all increments based on the values of `v[i]` for each `i` from `0` to `2 * n` across all iterations.
    #
    #This means that after all iterations of the loop have finished, `results` will contain a single string representing the final computed value of `ans`. The variable `cnt` will hold the total count of non-zero elements encountered in the list `v` across all iterations. The variable `idx` will point to the position right after the last processed element in the `data` list, which would be `3 * t + 1` since `t` is the number of iterations and we start processing from index 2. The variable `ans` will be the aggregated result of applying the given formulas to the lists `v` generated in each iteration.
    print('\n'.join(results))
    #This is printed: the final value of ans (where ans is the cumulative sum of all increments based on the values of v[i] for each i from 0 to 2 * n across all iterations)
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, an integer n, and a list a of n integers. For each test case, it calculates a specific value based on the frequency of elements in the list a and stores the result as a string in a list. Finally, it prints out these results, one per line.

