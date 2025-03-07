#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array a and the number of operations, respectively. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9, representing the array a. The sum of the values of n and k over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `t` retains its initial value as an input integer where 1 ≤ t ≤ 10^4. `j` is `t`, indicating that the loop has completed all `t` iterations. For each iteration, `b` is a list of strings from the input, `n` is the integer value of the first element in `b` and must be greater than 0, `k` is the integer value of the second element in `b`, and `l` is a list of integers from the input. `suf` is a list containing `n + 1` elements where the first element is 0 and each subsequent element is the sum of the previous element in `suf` and the corresponding element in `l`. `smin` is a list containing `n + 1` elements where each element is the minimum value of the suffix sums up to that index in `suf`. `sm` is the final computed value for each test case, which is printed, and it is calculated based on the conditions provided in the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` (the length of an array `a`) and an integer `k` (the number of operations). For each test case, it reads the array `a` and computes a value `sm` based on the suffix sums and minimum suffix sums of the array. The final value `sm` is adjusted using modular arithmetic and then printed. The function does not return any value; instead, it prints the result for each test case. After processing all test cases, the function completes, leaving the input variables `t`, `n`, `k`, and `a` in their final states as described in the annotations.

