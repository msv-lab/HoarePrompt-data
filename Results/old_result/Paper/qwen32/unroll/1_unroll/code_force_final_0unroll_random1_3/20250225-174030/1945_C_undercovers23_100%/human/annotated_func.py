#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses in the village, followed by a string a of length n consisting only of the characters '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: The smallest index where both '0's and '1's are at least 50% of the respective sub-strings for the last test case, or 0 or n based on the overall percentage of '1's if no such index exists.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of houses `n` and a string `a` of length `n` with '0's and '1's. It determines the smallest index where both '0's and '1's constitute at least 50% of their respective sub-strings. If no such index exists, it returns 0 if the overall percentage of '1's is at least 50%, otherwise it returns `n`.

