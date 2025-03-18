#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of non-negative integers such that 0 ≤ a_i ≤ n for all i where 1 ≤ i ≤ n. Additionally, the sum of all n values across all test cases does not exceed 3⋅10^5.
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
        
    #State: After the loop executes all its iterations, `i` will be equal to `n + 1`, `cnt` will be the sum of all elements in `v` (`sum(v)`), `ans` will be the sum of certain triangular and tetrahedral numbers based on the values in `v` that meet the criteria (specifically, for every `v[i] >= 3`, `ans` will include `v[i] * (v[i] - 1) * (v[i] - 2) // 6`, and for every `v[i] >= 2`, `ans` will include `cnt * v[i] * (v[i] - 1) // 2`), `n` remains unchanged, `results` will contain a string representation of `ans` for each iteration of the loop, and `idx`, `t`, and `results` remain in their initial states as they are not affected by the loop head and body.
    print('\n'.join(results))
    #This is printed: the string representation of `ans` for each iteration of the loop, separated by newlines
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (number of test cases), a positive integer \( n \) (size of the list), and a list of non-negative integers \( a \). For each test case, it calculates a specific value based on the frequency of each integer in the list \( a \). This value is derived from combinations of counts of integers appearing at least twice or three times. The function then stores these calculated values as strings in a list and prints them, one per line.

