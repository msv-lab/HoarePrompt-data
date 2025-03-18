#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4. For each test case, n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of the characters '0' and '1'. The sum of n over all test cases does not exceed 3 * 10^5.
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
        
    #State: After all iterations, `final` contains the optimal split point for each test case, ensuring that both halves of the string `s` have at least 50% '1's and '0's respectively.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of '0's and '1's. For each test case, it determines the optimal split point in the string such that both halves contain at least 50% of each character ('0' and '1'). If no such split exists, it returns either the start or end of the string based on the majority character.

