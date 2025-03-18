#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n positive integers such that 1 ≤ a_i ≤ n for all i. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: After the loop executes all the iterations, `ii` will be `n-1`, `cn` will be the total count of consecutive identical elements found in the list `num` from the beginning to the end, and `ck` will be the count of consecutive identical elements found in the reversed list `onum` from the beginning to the end. If the first element of `num` is equal to the first element of `onum`, `cn` will be incremented by `ck`. The variable `n` will remain unchanged, and the other variables (`r`, `f`, `num`, `j`, `onum`, `symb1`, `symb2`) will retain their final values from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t indicating the number of cases, an integer n representing the size of an array a, and the array a itself. For each test case, the function checks if the array contains any non-consecutive elements. If all elements are consecutive, it prints 0. Otherwise, it calculates the maximum length of consecutive identical elements in both the original and reversed arrays and prints the difference between the array size n and this maximum length.

