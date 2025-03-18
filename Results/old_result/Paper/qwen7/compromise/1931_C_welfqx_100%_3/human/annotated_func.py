#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: All variables outside the loop remain unchanged. The final value of `n` is the initial value of `t`. `cn` and `ck` are the maximum counts of consecutive identical elements found in the list `num` and its reverse `onum`, respectively, considering the entire list. `symb1` is `num[0]`, and `symb2` is `onum[0]`. The output of the loop is `n - max(cn, ck)`, which represents the minimum number of deletions required to make the list either entirely increasing or decreasing.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the list), and a list `a` of `n` integers. It then determines the minimum number of deletions required to make the list either entirely increasing or decreasing. The function outputs this minimum number of deletions for each test case.

