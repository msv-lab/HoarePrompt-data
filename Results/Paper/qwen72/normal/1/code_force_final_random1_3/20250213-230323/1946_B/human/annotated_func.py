#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array and the number of operations, respectively. The array a consists of n integers a_1, a_2, ..., a_n where -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all the iterations, `t` is 0, `j` is `t` (which is 0), `b`, `n`, `k`, `l`, `suf`, `smin`, and `sm` will have been updated for each test case according to the logic inside the loop. Specifically, for each test case, `b` is a list of strings from the input, `n` is the integer value of the first element in `b` and is greater than 0, `k` is the integer value of the second element in `b`, `l` is a list of integers from the input, `suf` is a list containing `n + 1` elements where each element at index `i` (for `i` from 1 to `n`) is the sum of the first `i` elements of `l`, `smin` is a list containing `n + 1` elements where each element at index `i` (from 0 to `n`) is the minimum value of `suf[j]` for all `j` from 1 to `i + 1`, and `sm` is the final computed value for the current test case, which is printed.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case includes an integer `n` (the length of an array), an integer `k` (the number of operations), and an array `a` of `n` integers. For each test case, the function computes a specific value based on the array and the number of operations, then prints the result modulo \(10^9 + 7\). The function processes all test cases and prints the results one by one. After processing all test cases, the function terminates.

