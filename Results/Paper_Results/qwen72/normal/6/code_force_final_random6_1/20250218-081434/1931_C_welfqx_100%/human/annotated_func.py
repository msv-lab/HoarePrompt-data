#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The sum of n for all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `r` is `t-1`, `n` is the last input integer greater than 1, `f` is 1, `num` is the last list of integers provided by the user, `j` is the index where the first inequality was found if the loop was broken, otherwise `j` is `n-2`, `onum` is a reversed copy of the last `num`, `symb1` is the first integer in the last `num`, `symb2` is the last integer in the last `num`, `i` is the index where the first inequality was found if the loop was broken, otherwise `i` is `n-2`, `ii` is the index of the last element checked in the last `onum` before the loop broke or completed, `ck` is the count of consecutive equal elements starting from the first element in the last `onum` up to the point where the first inequality was found or the end of the list. If `symb1` is equal to `symb2`, then `cn` is the count of consecutive equal elements starting from the first element in the last `num` up to the point where the first inequality was found or the end of the list plus the count of consecutive equal elements starting from the first element in the last `onum` up to the point where the first inequality was found or the end of the list.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `num`. It then determines the minimum number of elements that need to be removed from `num` to make it a palindrome. If the list is already a palindrome or contains only one element, it prints `0`. Otherwise, it calculates the maximum length of consecutive equal elements from the start and the end of the list, and prints the difference between the total number of elements `n` and this maximum length. After processing all test cases, the function terminates.

