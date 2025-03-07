#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the array elements. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it prints the minimum number of elements that need to be removed from the array to make it a palindrome. The variables `t`, `n`, and `a` (the array) are not directly modified by the loop, but the internal variables used within the loop (such as `f`, `num`, `onum`, `cn`, `ck`, `symb1`, and `symb2`) are reset and used for each test case. After all iterations, the initial state of `t`, `n`, and `a` remains unchanged, but the loop has printed the required output for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then calculates and prints the minimum number of elements that need to be removed from the list `a` to make it a palindrome. The function does not return any value; it only prints the results for each test case. After processing all test cases, the initial values of `t`, `n`, and `a` remain unchanged, but the function has printed the required output for each test case.

