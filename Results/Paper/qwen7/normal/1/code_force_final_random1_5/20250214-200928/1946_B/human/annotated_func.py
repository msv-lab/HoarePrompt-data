#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n, k ≤ 2 ⋅ 10^5, and the sum of the values of n and k for all test cases does not exceed 2 ⋅ 10^5. The array a is a list of n integers where -10^9 ≤ a_i ≤ 10^9 for each element a_i in the array.
def func():
    t = int(input())
    for j in range(t):
        b = input().split()
        
        n = int(b[0])
        
        k = int(b[1])
        
        l = list(map(int, input().split()))
        
        suf = []
        
        suf.append(0)
        
        for i in range(n):
            suf.append(suf[i] + l[i])
        
        smin = [0]
        
        for i in range(n):
            if suf[i + 1] < smin[i]:
                smin.append(suf[i + 1])
            else:
                smin.append(smin[i])
        
        sm = -111
        
        for i in range(n + 1):
            if suf[i] - smin[i] > sm or sm == -111:
                sm = suf[i] - smin[i]
        
        sm = 2 ** k * sm - sm
        
        sm += suf[n]
        
        if sm < 0:
            a = abs(sm) // (10 ** 9 + 7)
            sm += (a + 1) * (10 ** 9 + 7)
        else:
            sm = sm % (10 ** 9 + 7)
        
        print(sm)
        
    #State: Output State: The final output state after the loop executes all iterations will depend on the values of `t`, `k`, and the list `l`. However, based on the given information, we can infer the following:
    #
    #- The variable `sm` will be calculated as described in the loop logic.
    #- If `sm` is less than 0, it will be adjusted to 9999999995.
    #- Otherwise, `sm` will be taken modulo \(10^9 + 7\).
    #- After the loop completes, `sm` will be adjusted further based on its value: if `sm` is less than 0, it will be set to 9999999995; otherwise, it will be taken modulo 10.
    #
    #Given the specific output states after the first three iterations, we can deduce that the final value of `sm` will be 9999999995 if `sm` is less than 0, and otherwise, it will be the remainder of `sm` when divided by 10.
    #
    #Thus, the output state after the loop executes all the iterations is: **The value of `sm` will be either 9999999995 if it is less than 0, or the remainder of `sm` when divided by 10 otherwise.**
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, two integers n and k, and an array of n integers. For each test case, it calculates a value `sm` based on the array and the given parameters. If `sm` is less than 0, it sets `sm` to 9999999995; otherwise, it takes `sm` modulo \(10^9 + 7\). Finally, it prints the resulting value of `sm` for each test case.

