#State of the program right berfore the function call: The function `func` is expected to read input from stdin and write output to stdout. The input consists of multiple test cases, each with an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, followed by a string a of length n consisting only of 0 and 1, where a_j = 0 if the resident of the j-th house wants to live on the left side, and a_j = 1 if they want to live on the right side. The number of test cases t (1 ≤ t ≤ 2·10^4) is provided at the beginning of the input. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: The loop will process each test case and print the smallest index (1-based) where the percentage of residents wanting to live on the left side and the percentage of residents wanting to live on the right side are both at least 50%. If no such index exists, it will print 0 if the overall percentage of residents wanting to live on the right side is at least 50%, otherwise it will print n (the total number of houses). This process will be repeated for each test case, and the final output will be a series of integers, one for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` (the number of houses) and a string `a` of length `n` (representing the preferences of residents for living on the left or right side of their houses). For each test case, it calculates and prints the smallest index (1-based) where the percentage of residents wanting to live on the left side and the percentage of residents wanting to live on the right side are both at least 50%. If no such index exists, it prints 0 if the overall percentage of residents wanting to live on the right side is at least 50%, otherwise it prints `n` (the total number of houses). The function processes each test case independently and prints the result for each one.

