#State of the program right berfore the function call: Each test case consists of an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, followed by a string a of length n consisting only of the characters '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `a` of length `n` containing '0's and '1's. It determines the optimal position to divide the residents into two groups such that at least half of the residents on each side want to live on their respective sides. If no such position exists, it defaults to either the start or the end of the string based on the majority preference. The function outputs the position for each test case.

