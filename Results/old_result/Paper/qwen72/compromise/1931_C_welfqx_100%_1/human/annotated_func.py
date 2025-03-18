#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array. The array a contains n integers a_1, a_2, ..., a_n, where each a_i is an integer such that 1 <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `r` is `t - 1`, `n` is an input integer greater than 1, `f` is 1, `num` is a list of integers derived from the input, `onum` is a reversed copy of `num`, `symb1` is the first element of `num`, `symb2` is the last element of `num`, `cn` is the maximum number of consecutive elements from the start of `num` that are equal, `ck` is the maximum number of consecutive elements from the start of `onum` that are equal, and if `symb1` is equal to `symb2`, `cn` is `cn + ck`. The loop has printed `n - max(cn, ck)` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 <= t <= 10^4) representing the number of test cases. For each test case, it reads an integer `n` (1 <= n <= 2 * 10^5) representing the size of an array, and then reads `n` integers from the input to form the array `num`. The function determines the maximum number of consecutive identical elements from the start of `num` (`cn`) and from the end of `num` (`ck`). If the first and last elements of `num` are the same, it adds `ck` to `cn`. Finally, it prints `n - max(cn, ck)` for each test case. After processing all test cases, the function concludes.

