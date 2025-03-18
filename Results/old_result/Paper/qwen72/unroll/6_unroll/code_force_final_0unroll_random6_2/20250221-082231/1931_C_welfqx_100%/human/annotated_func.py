#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the array elements. The sum of n for all test cases does not exceed 2 * 10^5.
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
        
    #State: After the loop executes all the iterations, the variable `t` is decremented to 0, and the variables `n` and `num` are updated for each test case based on the input. The variables `f`, `onum`, `cn`, `ck`, `symb1`, and `symb2` are used within the loop to perform the necessary calculations and are reset for each test case. The output for each test case is printed, which is the result of `n - max(cn, ck)`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. The function then calculates the minimum number of elements that need to be removed from the list `a` to make it either a single element or a list where all elements are the same. The result for each test case is printed to the output. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the final state is that all test cases have been processed and their results printed.

