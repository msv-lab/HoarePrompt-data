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
        
    #State: Output State: t is an input integer, and after processing all inputs for n and the array a, the program prints the value of `n - max(cn, ck)` for each input, where `cn` and `ck` are calculated based on consecutive identical elements in the array and its reversed version.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases), an integer \( n \) (length of the array), and an array \( a \) of \( n \) integers. For each test case, it calculates the maximum length of consecutive identical elements in both the original and reversed arrays. It then prints the difference between the length of the array \( n \) and the maximum of these two lengths.

