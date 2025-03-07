#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n is a positive integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= n. The sum of n across all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop will have processed all `t` test cases, and the final values of the variables will reflect the last test case processed. The output will be a series of results printed for each test case, which is `n - max(cn, ck)` for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a list `a` of `n` integers. It then calculates and prints the value `n - max(cn, ck)`, where `cn` is the length of the longest prefix of the list that consists of identical elements, and `ck` is the length of the longest prefix of the reversed list that consists of identical elements. If all elements in the list are the same, it prints `0`.

