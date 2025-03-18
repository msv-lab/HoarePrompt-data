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
        
    #State: The output state will be a series of integers printed as the result of the loop's execution for each input. For each input, the program checks if all elements in the list are the same. If they are, it prints 0. Otherwise, it calculates the maximum length of consecutive identical elements from both the original and reversed list, adds these lengths if the first and last elements are the same, and then prints the difference between the length of the list and this sum.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` representing the number of test cases, followed by `t` sets of data. Each set consists of an integer `n` and a list of `n` integers. The function checks if all integers in the list are the same. If they are, it prints 0. Otherwise, it calculates the maximum length of consecutive identical elements from both the original and reversed list, adds these lengths if the first and last elements are the same, and then prints the difference between the length of the list and this sum. The function does not return any value but prints the results for each test case.

