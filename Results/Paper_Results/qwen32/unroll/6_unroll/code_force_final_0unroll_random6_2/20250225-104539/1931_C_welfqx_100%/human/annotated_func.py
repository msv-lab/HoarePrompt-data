#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= n. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    for r in range(t):
        n = int(input())
        
        f = 1
        
        num = [int(_) for _ in input().split()]
        
        for j in range(n - 1):
            if num[j] != num[j + 1]:
                f = 0
                break
        
        if n == 1 or f == 1:
            print(0)
            continue
        
        onum = num.copy()
        
        onum.reverse()
        
        cn = 1
        
        ck = 1
        
        f = 1
        
        symb1 = num[0]
        
        symb2 = onum[0]
        
        for i in range(n - 1):
            if num[i] == num[i + 1]:
                cn += 1
            else:
                break
        
        for ii in range(n - 1):
            if onum[ii] == onum[ii + 1]:
                ck += 1
            else:
                break
        
        if symb1 == symb2:
            cn += ck
        
        print(n - max(cn, ck))
        
    #State: After all iterations, the state of variables that are not affected by the loop (like `t`, the input values for the next test case, etc.) remains unchanged. The state of variables within the loop (like `f`, `num`, `onum`, `cn`, `ck`, `symb1`, `symb2`) will be reset at the start of each test case iteration. The only output is the series of integers printed for each test case.
    #
    #Since the question asks for the output state in a specific format and the output is a series of integers printed for each test case, the final output state can be described as the series of printed results for each test case.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints an integer value based on the list `a`. The printed value is the result of subtracting the maximum length of consecutive identical elements from the start or end of the list from `n`.

