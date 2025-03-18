#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and there are n non-negative integers a_1, \ldots, a_n where 0 ≤ a_j < 2^{31}. The sum of all n across all test cases does not exceed 2 \cdot 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: Output State: `t` remains a positive integer such that 1 ≤ t ≤ 10^4; `check` is 2147483647.
    #
    #Explanation: The loop processes a series of inputs but does not modify the values of `t` or `check`. The variable `t` is only defined in the initial state and is not altered within the loop. The variable `check` is set to `2147483647` at the start and remains unchanged throughout the loop executions. Therefore, both `t` and `check` retain their initial values after the loop completes all its iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` non-negative integers `a_1, ..., a_n` (where \(0 \leq a_j < 2^{31}\)). For each test case, it calculates and prints the count of unique elements in the list after performing bitwise XOR operations. The function does not return any value but prints the count for each sub-case. The variables `t` and `check` remain unchanged after processing all test cases.

