#State of the program right berfore the function call: The function should be called with no arguments, and it should internally handle multiple test cases. Each test case includes an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string a of length n consisting only of '0' and '1', where '0' indicates a resident who wants to live on the left side and '1' indicates a resident who wants to live on the right side. The function should read the input from standard input, where the first line contains the number of test cases t (1 ≤ t ≤ 2·10^4), and each subsequent test case is described by two lines: the first line contains n, and the second line contains the string a. The sum of n over all test cases does not exceed 3·10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        if n % 2 == 0:
            pk = n // 2
        else:
            pk = n // 2
        
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
            zero_perc = math.ceil(zero * 100 / (i + 1))
            one_perc = math.ceil((o - one) * 100 / (n - i - 1))
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
        
    #State: The function prints the optimal index for each test case where the percentage of residents on the left side who want to live on the left side and the percentage of residents on the right side who want to live on the right side are both at least 50%. If no such index exists, it prints either 0 or n, depending on which side has a majority of residents who want to live there. The loop iterates through all test cases and prints the result for each one.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` (3 ≤ n ≤ 3·10^5) and a string `a` of length `n` containing only '0' and '1'. For each test case, it calculates and prints the optimal index where the percentage of residents on the left side who want to live on the left side and the percentage of residents on the right side who want to live on the right side are both at least 50%. If no such index exists, it prints either 0 or `n`, depending on which side has a majority of residents who want to live there. The function processes and prints the result for each of the `t` (1 ≤ t ≤ 2·10^4) test cases.

