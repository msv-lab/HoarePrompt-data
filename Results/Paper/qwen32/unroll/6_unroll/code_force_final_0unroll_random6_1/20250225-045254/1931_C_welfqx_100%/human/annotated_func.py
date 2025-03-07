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
        
    #State: - After all `t` test cases are processed, the output will be a series of numbers, each corresponding to the result of one test case.
    #   - The state of the variables `t`, `n`, `num`, `f`, `onum`, `cn`, `ck`, `symb1`, and `symb2` will be based on the last iteration of the loop, but since the problem asks for the output state, we focus on the printed results.
    #
    #Since the output is a series of numbers printed for each test case, the output state can be described as a list of these results.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints a single integer value that represents the minimum number of elements to remove from the list so that all remaining elements are the same.

