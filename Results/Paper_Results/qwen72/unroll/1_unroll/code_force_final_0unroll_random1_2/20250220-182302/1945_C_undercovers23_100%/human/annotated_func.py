#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, where each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side and '1' indicates a preference to live on the right side. The function should also handle an input integer `t` (1 ≤ t ≤ 2·10^4) representing the number of test cases. The sum of `n` over all test cases does not exceed 3·10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n / 2
        else:
            pk = n / 2
        
        sl = list(s)
        
        o = sl.count('1')
        
        z = sl.count('0')
        
        zero, one = 0, 0
        
        lst = []
        
        mini = pow(10, 8)
        
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
            zero_perc = zero * 100 // (i + 1)
            one_perc = (o - one) * 100 // (n - i - 1)
            if zero_perc >= 50 and one_perc >= 50:
                lst.append(i + 1)
        
        for ele in lst:
            mini = min(mini, abs(pk - ele))
        
        final = []
        
        for elem in lst:
            if abs(pk - elem) == mini:
                final.append(elem)
        
        final.sort()
        
        if len(final) == 0:
            c1 = o * 100 // n
            if c1 >= 50:
                final.append(0)
            else:
                final.append(n)
        
        print(final[0])
        
    #State: The loop processes `t` test cases, and for each test case, it prints the smallest index (1-based) where the number of '0's and '1's on either side of the index (excluding the last house) are both at least 50% of the total number of houses on their respective sides. If no such index exists, it prints 0 if the total percentage of '1's is at least 50%, otherwise it prints `n` (the total number of houses).
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `a` of length `n` consisting of '0' and '1'. The function processes each test case to find the smallest index (1-based) where the number of '0's and '1's on either side of the index (excluding the last house) are both at least 50% of the total number of houses on their respective sides. If no such index exists, it prints 0 if the total percentage of '1's is at least 50%, otherwise it prints `n` (the total number of houses). The function prints the result for each test case.

