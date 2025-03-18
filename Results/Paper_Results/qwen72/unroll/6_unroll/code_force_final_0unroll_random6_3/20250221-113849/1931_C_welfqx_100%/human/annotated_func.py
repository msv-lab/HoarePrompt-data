#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases (1 ≤ t ≤ 10^4), and a list of lists, where each inner list represents a test case and contains n integers (1 ≤ n ≤ 2 · 10^5) for the array a, with each element a_i satisfying 1 ≤ a_i ≤ n. The sum of n for all test cases does not exceed 2 · 10^5.
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
        
    #State: The function will print the number of elements that need to be removed from each test case array to make it a palindrome, and the loop will complete all iterations for the given number of test cases `t`. The variables `r`, `n`, `f`, `num`, `onum`, `cn`, `ck`, `symb1`, and `symb2` will have their final values based on the last test case processed.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n` and a list of `n` integers. It then calculates the minimum number of elements that need to be removed from the list to make it a palindrome and prints this number for each test case. The function does not return any value but prints the results directly. After processing all test cases, the function completes, and the state of the program reflects the final values of the variables based on the last test case processed.

