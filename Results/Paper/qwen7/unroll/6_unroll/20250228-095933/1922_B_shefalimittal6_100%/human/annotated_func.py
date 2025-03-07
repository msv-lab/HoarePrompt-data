#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 3⋅10^5, and the list a contains n integers where each integer a_i satisfies 0 ≤ a_i ≤ n. Additionally, the sum of all n values over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: `idx` is 6, `t` is an integer equal to `int(data[0])`, `results` is a list containing the calculated answers for each iteration.
    print('\n'.join(results))
    #This is printed: what is printed (where the printed content is the elements of the `results` list, each on a new line)
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t indicating the number of test cases, an integer n indicating the size of the list a, and a list a of n integers. For each test case, it calculates a value based on the frequency of each integer in the list a and appends the result to a list. Finally, it prints each result from the list on a new line.

