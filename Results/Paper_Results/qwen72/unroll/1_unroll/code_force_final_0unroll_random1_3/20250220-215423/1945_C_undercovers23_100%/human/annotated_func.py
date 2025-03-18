#State of the program right berfore the function call: The function `func` is intended to process multiple test cases. Each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident who wants to live on the left side and '1' indicates a resident who wants to live on the right side. The function should be called with these inputs provided in a structured format, such as a list of tuples or a similar data structure that can hold the test cases. The total sum of `n` over all test cases does not exceed 3·10^5.
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
        
    #State: The loop processes all test cases and prints the smallest index (1-based) for each test case where the percentage of '0's up to that index and the percentage of '1's after that index are both at least 50%. If no such index exists, it prints 0 if the overall percentage of '1's is at least 50%, otherwise it prints `n`. The variables `t`, `n`, `s`, `sl`, `o`, `z`, `zero`, `one`, `lst`, `mini`, and `final` are reset and updated for each test case, and the final output for each test case is printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` (3 ≤ n ≤ 3·10^5) and a string `a` of length `n` consisting only of '0' and '1'. For each test case, it finds the smallest index (1-based) where the percentage of '0's up to that index and the percentage of '1's after that index are both at least 50%. If no such index exists, it prints 0 if the overall percentage of '1's is at least 50%, otherwise it prints `n`. The function does not return any value; it prints the result for each test case directly.

